
import csv

with open("sample.csv", "r") as fin:
    csv_in = csv.reader(fin)
    data = list(csv_in)

data = [[int(x) for x in y] for y in data] # note this is a bit advanced; you could also use nester for loop

with open("output.csv", "w") as fout:
    csv_out = csv.writer(fout)
    for row in data:
        csv_out.writerow([sum(row)])
