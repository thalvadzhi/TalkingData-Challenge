import csv
import random

file_reader = open("D:\\DataSetFiles\\Project-DM\\train.csv", "r", encoding="ascii")

read = csv.reader(file_reader, delimiter=",")
row1 = next(read)

file = open("downsampling_train.csv", "w")
writer = csv.writer(file, delimiter=',', lineterminator='\n')
writer.writerow(row1)


i = 0
positive_examples = 4600000

for row in read:
    if (int)(row[-1]) == 1:
        writer.writerow(row)
        i += 1
    else:
        if random.uniform(0,1) <= 0.0556:
            writer.writerow(row)
            i += 1

file.close()

print('examples are: ', i)
print('done.')
