import csv

file_reader = open("D:\\DataSetFiles\\Project-DM\\test.csv", "r", encoding="ascii")

max_rows = 100000
read = csv.reader(file_reader, delimiter=",")

file = open("new_test_set.csv", "w")
writer = csv.writer(file, delimiter=',', lineterminator='\n')

i = 0
for row in read:
    writer.writerow(row)
    i += 1
    if i > max_rows:
        break

file.close()