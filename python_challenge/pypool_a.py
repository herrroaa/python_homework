import csv
csvpath= "election_data_1.csv"

with open (csvpath, newline="") as csvfile:
    datafile = csv.reader(csvfile, delimiter=',')
    next(datafile,None)
    print (datafile)

    for row in datafile:
        votes=int(row[0])

    
    def sum(numbers):
        sum = 0
        for row in range(votes):
            sum += row
        return sum

total=sum(votes)    
print( "the total number of votes " + str(total))



