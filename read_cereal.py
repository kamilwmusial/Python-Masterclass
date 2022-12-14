import csv

csv_filename = 'cereal_grains.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    # csv.QUOTE_NONNUMERIC - instructs reader to convert all non-quoted fields to type float
    for row in reader:
        print(row)