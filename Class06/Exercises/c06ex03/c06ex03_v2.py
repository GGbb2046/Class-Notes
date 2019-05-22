
import csv

with open("sample.csv", "r") as fin:
    csv_in = csv.reader(fin)
    data = list(csv_in)

# print(data)

for row in range(len(data)):
    for column in range(len(data[row])):
        data[row][column]=int(data[row][column])

# print(data)

with open("output.csv", "w") as fout:
    csv_out = csv.writer(fout)
    for row in data:
        csv_out.writerow([sum(row)])
