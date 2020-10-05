import pycounter
from datetime import datetime

now = datetime.now()

import datetime
import time
import csv



initial_year = input('ano inicial: ')
initial_month = input('mes inicial: ')
initial_day = 1
print('dia inicial: 1')

final_year = input('ano final: ')

final_month = input('mes final: ')

final_day = input('dia final: ')

initial_date = datetime.date(int(initial_year), int(initial_month), int(initial_day))
final_date = datetime.date(int(final_year), int(final_month), int(final_day))

range = str(initial_date) + " " + str(final_date)

print('Range: ' + range)
log = str(now) + range + "\n"

with open('editoras-CR.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print('Lendo CSV')
    log = str(now) + "Lendo CSV \n"
    
    publisher = []    
    sushiURL = []    
    requestorID = []
    costumerNumber = []
    for row in readCSV:
        publisher = row[0]
        print('Harvesting editora: ' + publisher)
        log = str(now) + "Harvesting " + publisher + "\n "
        
        sushiURL = row[1]
        requestorID = row[2]
        costumerNumber = row[3]

        print("Em progresso")
        log = str(now) + "Em progresso\n"
        resultado = pycounter.sushi.get_sushi_stats_raw(sushiURL,initial_date,final_date,requestorID,"Capes1",None,costumerNumber,None,"CR1",4,False,True)
        print("Concluído")
        log = str(now) + "Concluído \n"
        resultado = str(resultado)
        resultado = resultado[2:]
        resultado = resultado[:-1]

        print("Escrevendo dados em arquivo\n ---------------\n---------------\n---------------\n \n")
        log = str(now) + "Escrevendo dados em arquivo \n"
        
        filename = publisher + '.xml'
        
        f = open(filename,'w')
        f.write(resultado)
        f.close()

        from datetime import date
        
        today = date.today()
        
        filename = "harvesting" + str(today) + ".log"

        f = open(filename,'w')
        f.write(log)
        f.close()

