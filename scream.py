from csv import reader, writer

with open('fighter.csv') as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row ] for row in csv_reader]
    for row in fighters:
        print(row)

with open("screaming_fighter.csv", "w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)

# alternate method

with open('fighters.csv') as file:
    csv_reader = reader(file)
    with open("screaming_fighter.csv", "w") as file:
    csv_writer = writer(file)
        for fighter in csv_reader:
        csv_reader.writerow([s.upper() for s in fighter])
