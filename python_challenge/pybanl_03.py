import csv
csvpath= "budget_data_1.csv"

with open (csvpath, newline="") as csvfile:
    datafile = csv.reader(csvfile, delimiter=',')
    total =0 
    # To get the avrage revenue across entire period 

    next(datafile,None)
    for row in datafile:
        total =+ int(row[1])
    print (total)       

length = len(row[1])
average= total /length
print("The average revenue across entire period is " + str(average))