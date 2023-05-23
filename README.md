# ListaWebApp

Aplicação web consistindo de uma lista de tarefas com nome, custo e data de validade, cuja persistência dos dados é garantida por um container com um banco de dados.

## Passos para configurar seu ambiente:

#### Passo 1) Clonar o repositório com o comando:

>**git clone <linkdorepositório>**

#### Passo 2) Instalar o docker ce e o docker-compose mais atuais para seu sistema atual;

## Passos para criar os containers após o clone:

- Na primeira execução, é preciso criar as tabelas no banco após subir os containers. Siga os passos abaixo.

#### Passo 1) Executar o comando abaixo e aguardar o mysql terminar de criar o container
>**docker-compose up**

#### Passo 2) Executar o script setup.sh para criar a tabela
>**./setup.sh**

- O passo 2 só é necessário na primeira execução do programa, pois uma vez criadas as tabelas, elas ficarão salvas na pasta.

***

## Hostear a aplicação no local host:

#### Iniciar os containers com o comando:
   > **docker-compose up -d**

##### ***Os seguintes containers devem estar rodando na sua máquina:***

	mysql -> container do banco de dados;
	memcached -> container para gerenciar um cache local;
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
