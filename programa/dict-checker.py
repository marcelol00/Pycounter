import pycounter
from datetime import datetime
import os, sys
import json
import datetime
import time
import csv

""" 
Solicitação de atribuição de data
Formato deve ser inteiro, YYYYMMDD e o dias iniciais e finais 01 e último dia do mês, respectivamente.

"""

"""
initial_year = input('ano inicial: ')
initial_month = input('mes inicial: ')
initial_day = 1
print('dia inicial: 1')

final_year = input('ano final: ')

final_month = input('mes final: ')

final_day = input('dia final: ')
"""

##Atribui a data automaticamente para acelerar o processo de teste

initial_year = 2020
initial_month = 1
initial_day = 1

final_year = 2020

final_month = 5

final_day = 31

## jutando os dados à variáveis finais de data 
initial_date = datetime.date(int(initial_year), int(initial_month), int(initial_day))
final_date = datetime.date(int(final_year), int(final_month), int(final_day))

##Escrevendo o a data na tela de prompt
range = str(initial_date) + " " + str(final_date)
print('Range: ' + range)

pathToCredentials = "C:\\Users\\marce\\Documents\\Programação\\Python\\Pycounter\\Arquivos\\sushi-credentials\\" 

## siglaDaEditora = input("Qual a sigla da editora? ")

"""
Se o valor de siglaDaEditora for TODOS, o programa lerá todos os arquivos na pasta indicada em pathToCredentials, pegando as credenciais SUSHI 5 para colher as estatísticas

Caso a variável siglaDaEditora possua outro valor, ele pulará para o else, que concaternará pathToCredentials + siglaDaEditora + csv que deverá formar o caminho para o arquivo de credentials dessa única editora.

"""
"""
if siglaDaEditora == "TODOS":
    ## Lê os arquivos na pasta e percorre a lista com os nomes dos arquivos. Cuidado para não colocar outros arquivos nessa pasta que não seja os de credenciais de SUSHI.
    dirs = os.listdir(pathToCredentials)
    for file in dirs:
        ## print para debug
        print(file)
        
        ## Lê um dos arquivos na pasta que deve ter as informações conforme a ordem abaixo:
        """
dirs = os.listdir(pathToCredentials)
for file in dirs:        
    with open(pathToCredentials + file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        print('Lendo CSV' + file)
        
        publisher = []    
        sushiURL = []    
        requestorID = []
        costumerNumber = []
        api_key = []

        for row in readCSV:
            publisher = row[0]
            sushiURL = row[1]
            requestorID = row[2]
            costumerNumber = row[3]
            api_key = row[4]
            print('Harvesting editora: ' + publisher + " - " + costumerNumber)
            print("Em progresso")
            ## Comando que extrai o json da editora e o transforma em dict, conforme veremos no comando print(type()) abaixo
            counter5Json = pycounter.sushi5.get_sushi_stats_raw(
                None,
                initial_date,
                final_date,
                requestorID,
                costumerNumber,
                "TR_J1",
                5,
                True,
                True,
                sushiURL,
                api_key
                )
            print(type(counter5Json))
            
            counter5JsonKeys = dict.keys(counter5Json)
            print(counter5JsonKeys)

"""
                ## A função raw_to_full() transforma o dict obtido com o editor em um objeto CounterReport. Isso é porque os mantenedores não desenvolveram um relatório no padrão Counter5 e então adaptam os dados para a saída em Counter4 que eles já tinham pronta.
                objectCounterReport = pycounter.sushi5.raw_to_full(counter5Json)
                print(type(objectCounterReport))

                ## Caminho para a pasta onde será gravada o TSV na função write_tsv()
                pathToTSVfile = "C:\\Users\\marce\\Documents\\Programação\\Python\\Pycounter\\Arquivos\\Estatísticas\\" + costumerNumber + ".tsv"

                print("Escrevendo dados em arquivo\n---------------\n")
                        
                pycounter.report.CounterReport.write_tsv(objectCounterReport,pathToTSVfile)
                print("\n---------------\n")
                print("\n---------------\n")
                print("\n---------------\n")

"""                
## Para cá vem o programa quando o valor da variável editora não é TODOS

"""
elif siglaDaEditora != "TODOS":
    ## Lê um dos arquivos na pasta que deve ter as informações conforme a ordem abaixo:
    with open(pathToCredentials + siglaDaEditora + '.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        print('Lendo CSV')
        
        publisher = []    
        sushiURL = []    
        requestorID = []
        costumerNumber = []
        api_key = []

        for row in readCSV:
            publisher = row[0]
            sushiURL = row[1]
            requestorID = row[2]
            costumerNumber = row[3]
            api_key = row[4]
            print('Harvesting editora: ' + publisher + costumerNumber)
            print("Em progresso")
            ## Comando que extrai o json da editora e o transforma em dict, conforme veremos no comando print(type()) abaixo
            counter5Json = pycounter.sushi5.get_sushi_stats_raw(
                None,
                initial_date,
                final_date,
                requestorID,
                costumerNumber,
                "TR_J1",
                5,
                True,
                True,
                sushiURL,
                api_key
                )

            print(type(counter5Json))
            
            ## A função raw_to_full() transforma o dict obtido com o editor em um objeto CounterReport. Isso é porque os mantenedores não desenvolveram um relatório no padrão Counter5 e então adaptam os dados para a saída em Counter4 que eles já tinham pronta.
            objectCounterReport = pycounter.sushi5.raw_to_full(counter5Json)
            print(type(objectCounterReport))

            ## Caminho para a pasta onde será gravada o TSV na função write_tsv()
            path = "C:\\Users\\marce\\Documents\\Programação\\Python\\Pycounter\\Arquivos\\Estatísticas\\" + costumerNumber + ".tsv"
            
            print("Escrevendo dados em arquivo\n \n \n---------------\n \n")
                    
            pycounter.report.CounterReport.write_tsv(objectCounterReport,path)
            print("\n---------------\n")
            print("\n---------------\n")
            print("\n---------------\n")

"""
        