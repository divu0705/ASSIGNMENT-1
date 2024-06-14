# read from csv file
import csv

with open('divya.csv', newline=' ') as f:
    a = csv.reader(f, delimiter=' ')
    for row in a:
        print(row)

