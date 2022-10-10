from flask import Flask, jsonify, request, abort, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
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

@app.route("/")
def index():
    return render_template("index.html", tarefas = Tarefa.query.all())

#POST FROM WEBSITE
@app.route('/add_tarefa/', methods=['POST'])
def add_tarefa():
    if not request.form:
        abort(400)
    tarefa = Tarefa(
        tarNome=request.form.get('tarNome'),
        dataLimite=request.form.get('dataLimite'),
        custo=request.form.get('custo')
    )
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
        abort(404)
    tarefa.tarNome = request.form.get('tarNome', tarefa.tarNome)
    tarefa.dataLimite = request.form.get('dataLimite', tarefa.dataLimite)
    tarefa.custo = request.form.get('custo', tarefa.custo)
    db.session.commit()
    return redirect(url_for("index"))

#DELETE FROM WEBSITE
@app.route("/delete/<int:tarId>", methods=["POST"])
def delete(tarId):
    tarefa = Tarefa.query.get(tarId)
    if tarefa is None:
        abort(404)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for("index"))
