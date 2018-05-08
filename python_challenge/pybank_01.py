
import csv
csvpath= "budget_data_1.csv"
total_revenue=0.0
max_revenue=0.0
min_revenue=0.0
average_revenue=0.0


with open (csvpath, newline="") as csvfile:
    datafile = csv.reader(csvfile, delimiter=',')
    print(datafile)
    next(datafile,None)
    number_months = len(list(datafile))


with open (csvpath, newline="") as csvfile:
    datafile = csv.reader(csvfile, delimiter=',')
    print(datafile)
    next(datafile,None)
    for row in datafile:
        value= float(row[1])
        total_revenue=total_revenue + value
        average_revenue=total_revenue/ number_months
        max_revenue=(max(max_revenue,value))
        min_revenue=(min(min_revenue,value))

print ( "The total number of months inclued in the dataset is " + str(number_months) \
    + " . The total amount of revenue gained over the entire period is " + str(total_revenue) \
    + " . The average change in revenue between months over the entire period " + str(average_revenue) \
     + " . The total revenue the greatest increase in revenue gained over the entire period is " + str(max_revenue) \
  + " . and The total revenue the greatest increase in revenue gained over the entire period is " + str(min_revenue)) 