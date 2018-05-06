#To get The total number of months included in the dataset, 
# count the rows without the header
import csv
csvpath= "budget_data_1.csv"


with open (csvpath, newline="") as csvfile:
    datafile = csv.reader(csvfile, delimiter=',')
    print(datafile)
    next(datafile,None)
    months_num = list(datafile)
    print(months_num)
    #row_count = len(months_num)
    #print("the total number of months inclued in the dataset is " + str(row_count)) 