#!/bin/bash
#Cria a tabela Tarefas
docker-compose exec mysql-app mysql -puser -e"create table IF NOT EXISTS listaApp.Tarefas(tarId int primary key auto_increment, tarNome varchar(255) not null unique, custo decimal(10, 2), dataLimite date, ordem int)"
