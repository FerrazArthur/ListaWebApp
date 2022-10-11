#!/bin/bash
#Execute esse arquivo antes de criar os containers pela primeira vez, 
#ele permitirá que o mysql seja configurado corretamente na pasta do projeto.
#Existe um segundo arquivo chamado setup2.sh que é pra ser executado uma vez que
#o container mysql tenha criado seus arquivos corretamente.
cp database/listaApp/Tarefas.ibd .

sudo rm -r database