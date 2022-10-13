# ListaWebApp
Aplicação feita para processo seletivo da empresa Fatto
pra iniciar o ambiente:

## Passos para configurar seu ambiente:

#### Passo 1) Clonar o repositório com o comando:

>**git clone linkdorepositório**

#### Passo 2) Instalar o docker ce e o docker-compose mais atuais para seu sistema atual;

## Passos para criar os containers após o clone:

#### Passo 3) Executar o comando abaixo e aguardar o mysql terminar de criar o container
>**docker-compose up**

#### Passo 4) Executar o script setup.sh para criar a tabela
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