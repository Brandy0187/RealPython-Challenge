import os
import csv
budget_csv = os.path.join(".", "Module 03 Challenge", "PyBank", "Resouces", "budget_data.csv")

 #open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
numMonths = set()

    #Reading the csv file
csv_header = next(csv_file)
total = 0

    #Counting the month/date row
for row in csv_reader:
    numMonths.add(row[0])
print(len(numMonths))

    #Count total profit/loss
for row in csv.reader(csv_file):
    total += int(row[1])
print (total)

#identify the change in profit/loss and return avg

#find per month total
