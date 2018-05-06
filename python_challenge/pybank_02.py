

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

#to get the avrage revenue across entire period
#length = len(row[1])
#average= total /length
#print(average)


#to ge The greatest increase  and greatest deccrease in revenue (date and amount) over the entire period
#def min_max(x):
 #   return min(x), max(x)
#great_inc_dec= min_max(total)
#print(total)
