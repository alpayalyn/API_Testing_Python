import csv

with open('utilities/cardapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',') # csv Reader object, I need to convert it to a list.
    # print(csvReader)
    # print(list(csvReader))

    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])
    print(names)
    print(stats)
    Index = names.index('Joe')
    loanStatus = stats[Index]
    print('loan status is' + loanStatus)

    with open('utilities/cardapp.csv','a') as wFile:
        write = csv.writer(wFile)
        write.writerow(["Kazim", "Rejected"])