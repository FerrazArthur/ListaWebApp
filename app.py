from flask import Flask, jsonify, request, abort, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_cors import CORS
import os

#config
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

#init
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    return app

#models
class Tarefa(db.Model):
    __tablename__ = 'Tarefas'
    tarId = db.Column(db.Integer, primary_key=True)
    tarNome = db.Column(db.String(255), nullable=False)
    custo = db.Column(db.Float(10))
    dataLimite = db.Column(db.Date())
    ordem = db.Column(db.Integer)
    def to_json(self):
        return {
            'tarId': self.tarId,
            'tarNome': self.tarNome,
            'custo': self.custo,
            'dataLimite': self.dataLimite,
            'ordem': self.ordem
        }

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
bootstrap = Bootstrap(app)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html", tarefas = Tarefa.query.order_by(Tarefa.ordem).all())

#POST FROM WEBSITE
@app.route('/add_tarefa/', methods=['POST'])
def add_tarefa():
    if not request.form:
        abort(400)
    nometemp=request.form.get('tarNome')
    if Tarefa.query.filter_by(tarNome=nometemp).first() is not None:
        abort(400, 'Erro de entrada: O nome '+nometemp+' já esta sendo utilizado por uma tarefa. Por favor tente outro nome')
    
    tarefa = Tarefa(
        tarNome=nometemp,
        dataLimite=request.form.get('dataLimite'),
        custo=request.form.get('custo'),
        ordem=Tarefa.query.count()+1
    )
    if tarefa.dataLimite == '':
        tarefa.dataLimite = None
    db.session.add(tarefa)
    db.session.commit()
    return redirect(url_for("index"))

#PUT FROM WEBSITE
@app.route('/update_tarefa/<int:tarId>', methods=['POST'])
def update_tarefa(tarId):
    if not request.form:
        abort(400)
    tarefa = Tarefa.query.get(tarId)
    if tarefa is None:
        abort(400)
    nometemp = request.form.get('tarNome', tarefa.tarNome)
    if tarefa.tarNome != nometemp and Tarefa.query.filter_by(tarNome=nometemp).first() is not None:
        abort(400, 'Erro de entrada: O nome '+nometemp+' já esta sendo utilizado por uma tarefa. Por favor tente outro nome')
    else:
        tarefa.tarNome=nometemp
    tarefa.dataLimite = request.form.get('dataLimite', tarefa.dataLimite)
    tarefa.custo = request.form.get('custo', tarefa.custo)
    db.session.commit()
    return redirect(url_for("index"))

#PUT FROM WEBSITE TO CHANGE PRIORITY
@app.route('/update_priority/<int:tarId>/<int:tarId2>', methods=['POST'])
def update_priority(tarId, tarId2):
    '''Troque a prioridade entre as duas tarefas.
    Se ordem de tarId > ordem de tarId2: incrementa 1 em todas tarefas entre tarId2 e a antiga posição de tarId
    Se ordem de tarId < ordem de tarId2: decrementa 1 em todas tarefas entre tarId2 e a antiga posição de tarId'''

    # Atualizar a ordem das tarefas no caminho da alteração
    tarefaTemp1=Tarefa.query.get(tarId)
    tarefaTemp2=Tarefa.query.get(tarId2)
    
    if tarefaTemp1 is None or tarefaTemp2 is None:
        abort(404, 'Tarefas não encontradas')

    ordemTemp=tarefaTemp2.ordem

    if tarefaTemp1.ordem == tarefaTemp2.ordem:
        abort(404, 'A Ordem das tarefas devem ser diferentes')
    elif tarefaTemp1.ordem > tarefaTemp2.ordem:
        tarefasApos = Tarefa.query.filter(Tarefa.ordem >= tarefaTemp2.ordem, Tarefa.ordem < tarefaTemp1.ordem).all()
        for tarefa in tarefasApos:
            tarefa.ordem += 1
    else:
        tarefasApos = Tarefa.query.filter(Tarefa.ordem <= tarefaTemp2.ordem, Tarefa.ordem > tarefaTemp1.ordem).all()
        for tarefa in tarefasApos:
            tarefa.ordem -= 1

    #Atualizando ordem da tarefa tarId
    tarefaTemp1.ordem=ordemTemp
    db.session.commit()
    return jsonify(success=True)

#DELETE FROM WEBSITE
@app.route("/delete/<int:tarId>", methods=['POST'])
def delete(tarId):
    tarefa = Tarefa.query.get(tarId)
    if tarefa is None:
        abort(404)
    
    # Atualizar a ordem das tarefas após a removida
    tarefasApos = Tarefa.query.filter(Tarefa.ordem > tarefa.ordem).all()
    for tarefaApos in tarefasApos:
        tarefaApos.ordem -= 1

    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for("index"))

#PUT
@app.route('/tarefa/<int:tarId>', methods=['PUT'])
def update2_tarefa(tarId):
    if not request.json:
        abort(400)
    tarefa = Tarefa.query.get(tarId)
    if tarefa is None:
        abort(404)
    tarefa.ordem = request.json.get('ordem', tarefa.ordem)
    db.session.commit()
    return jsonify(tarefa.to_json())

