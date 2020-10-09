import pycounter
from datetime import datetime

now = datetime.now()

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
log = str(now) + range + "\n"

with open('editoras-counter5.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print('Lendo CSV')
    log = str(now) + "Lendo CSV \n"
    
    publisher = []    
    sushiURL = []    
    requestorID = []
    costumerNumber = []
    api_key = []
    for row in readCSV:
        publisher = row[0]
        print('Harvesting editora: ' + publisher)
        log = str(now) + "Harvesting " + publisher + "\n "
        
        sushiURL = row[1]
        requestorID = row[2]
        costumerNumber = row[3]

        print("Em progresso")
        log = str(now) + "Em progresso\n"
        resultado = pycounter.sushi.get_sushi_stats_raw(
            sushiURL,
            initial_date,
            final_date,
            requestorID,
            "Capes1",
            None,
            costumerNumber,
            None,
            "JR1",
            4,
            False,
            True
            )
        print(resultado)

        path = "C\:\\Users\\marce\\Documents"
        format_= "TSV"
        
        pycounter.report.CounterReport.write_to_file(path,format_)

        print("Escrevendo dados em arquivo\n ---------------\n---------------\n---------------\n \n")
        
        filename = publisher + '.xml'
        
        f = open(filename,'w')
        f.write(resultado)
        f.close()
