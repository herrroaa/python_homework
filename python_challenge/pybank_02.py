

import csv
csvpath= "budget_data_1.csv"

with open (csvpath, newline="") as csvfile:
    datafile = csv.reader(csvfile, delimiter=',')
    total = 0 
    next(datafile,None)
    print (datafile)

 
 #To get the total amount of revenue gained over the entire period  
    for row in datafile:
        total =+ int(row[1])
    print( "the total amount of revenue gained over the entire period is " + str(total))


