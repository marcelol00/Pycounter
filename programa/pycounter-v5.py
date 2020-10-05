import pycounter
from datetime import datetime

import json
import datetime
import time
import csv


"""
initial_year = input('ano inicial: ')
initial_month = input('mes inicial: ')
initial_day = 1
print('dia inicial: 1')

final_year = input('ano final: ')

final_month = input('mes final: ')

final_day = input('dia final: ')
"""

initial_year = 2020
initial_month = 1
initial_day = 1

final_year = 2020

final_month = 5

final_day = 31

initial_date = datetime.date(int(initial_year), int(initial_month), int(initial_day))
final_date = datetime.date(int(final_year), int(final_month), int(final_day))

range = str(initial_date) + " " + str(final_date)

print('Range: ' + range)

with open('editoras-counter5.csv') as csvfile:
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
        resultado = pycounter.sushi5.get_sushi_stats_raw(
            None,initial_date,
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

        print(type(resultado))

        object_report = pycounter.sushi5.raw_to_full(resultado)
        print(type(object_report))
        path = "C:\\Users\\marce\\Documents\\Novapasta\\" + costumerNumber + ".tsv"

        print("Escrevendo dados em arquivo\n \n \n---------------\n \n")
                
        pycounter.report.CounterReport.write_tsv(object_report,path)

