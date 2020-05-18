# from csv import reader

# with open("fighter.csv") as file:
#     csv_reader = reader(file)
#     for f in csv_reader:
#         print(f"{f[0]} is from {f[1]}")




from csv import DictReader
# using a DictReader
with open("fighter.csv") as file:
    csv_reader = DictReader(file)
    for f in csv_reader:
        print(f['Name'])