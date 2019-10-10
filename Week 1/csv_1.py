import csv
with open('c1.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['Country'])
    
    with open('c2.csv','w') as fname2:
        fields=['A','B','C']
        csv_writer = csv.DictWriter(fname2,fieldnames=fields)

        for line in csv_reader:
            csv_writer.writerow(line)

