import csv
csvpath= "election_data_1.csv"

candidate=[]
word=

with open (csvpath, newline="") as csvfile:
    datafile = csv.reader(csvfile, delimiter=',')
    next(datafile,None)



#To get a complete list of candidates who received votes
    for row in datafile:
        if float(row[0]) > 0:
            if word not in candidate:
                candidate.append(row[2])
       
print(candidate)
#print(losers)

#number_of_candidates_received_votes=len(candidate)
#print(number_of_candidates_received_votes)







