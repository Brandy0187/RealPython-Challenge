import os
import csv

budget_csv = os.path.join("budget_data.csv")

 #open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #print(csv_reader)
    

    #Reading the csv file and ignore the header
    csv_header = next(csv_file)
    numMonths = set()

     #Counting the month/date row
    for row in csv_reader:
        numMonths.add(row[0])
    #print (len(numMonths))

#Calculate the total profit/loss
    pft_loss = (float (row[1]) for row in csv_reader)
    total = sum(pft_loss)
    print (total)

#
# #identify the change in profit/loss and return avg


