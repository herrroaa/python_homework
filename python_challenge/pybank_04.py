

import csv
csvpath= "budget_data_1.csv"

with open (csvpath, newline="") as csvfile:
    datafile = csv.reader(csvfile, delimiter=',')
    next(datafile,None)
    print (datafile)
    
    for row in datafile: 
        value=int(row[1])
        #print(value)

    def min_max(numbers):
        for row in range(value):
            min_max(int(row)
        return min(numbers), max(numbers)

both = min_max(value)
print(both)

#min(value)
#to ge The greatest increase  and greatest deccrease in revenue (date and amount) over the entire period
#great_dec= min(value)
#print(great_dec)
#res=value[int(great_dec)]
#print(res)



