# ListaWebApp
Aplicação feita para processo seletivo da empresa Fatto
pra iniciar o ambiente:

## Passos para configurar seu ambiente:

#### Passo 1) Clonar o repositório com o comando:

>**git clone linkdorepositório**

#### Passo 2) Instalar o docker ce e o docker-compose mais atuais para seu sistema atual;

## Passos para criar os containers após o clone:

#### Passo 1) Executar o arquivo setup1.sh

#### Passo 2) Executar o comando abaixo e aguardar o mysql terminar de criar o container
>**docker-compose up**

<<<<<<< HEAD
##### Passo 3) Executar a criação da tabela Tarefas seguindo os comandos
>**docker exec -it mysql mysql -p** (entre com a senha -> user)

>**create table listaApp.Tarefas(tarId int primary key auto_increment, tarNome varchar(255) not null unique, custo decimal(10, 2), dataLimite date, ordem int);**

>**exit**

##### Passo 4) Executar o arquivo setup2.sh
=======
#### Passo 3) Executar os comandos abaixo, em outro terminal, para criar a tabela
>**docker exec -it mysql -p** 

>**create table listaApp.Tarefas(tarId int primary key auto_increment, tarNome varchar(255) not null unique, custo decimal(10, 2), dataLimite date, ordem int);**

#### Passo 4) Saia do container e execute o arquivo setup2.sh para que as tarefas salvas no git estejam disponíveis na sua maquina
>>>>>>> 3bc3382af90f5346e74a257e924cb46ea66527d9

***

## Hostear a aplicação no local host:

#### Iniciar os containers com o comando:
   > **docker-compose up**

##### ***Os seguintes containers devem estar rodando na sua máquina:***

	mysql -> container do banco de dados;
	tarefas-app -> container da aplicação.

### O site estará acessivel através do link:

>**http://172.17.0.1:8000**;

## Para trabalhar no projeto e submeter pull requests:

- ***Você precisa de fazer um fork do projeto para seu repositório***

#### Depois, no terminal na pasta do seu projeto dê o comando: 

>git remote add **seunome** **linkdofork**

#### Criar uma branch

>git checkout -b **nomebranch**

#### Quando solicitado "Dar pull":

>git pull origin **nomebranch**

#### Ao concluir uma tarefa:

>git add .
git commit -m **nomedocommit**
git push **seunome** **nomebranch**