import csv
csvpath= "budget_data_1.csv"

with open (csvpath, newline="") as csvfile:
    datafile = csv.reader(csvfile, delimiter=',')
    total =0 
    #To get The total number of months included in the dataset /
    #count the rows without the header
    next(datafile,None)
    next(datafile,None)
    #req = list(datafile)
    #row_count = len(req)
    #print(row_count)
    #print(datafile)
    
    for row in datafile:
        total =+ int(row[1])
    print (total)        
        
       
    