# # Not good 
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     for row in csv_reader:
#         # each row is list
#         print(row)

# using reader
from csv import reader
with open("fighter.csv")as file:
    csv_reader = reader(file)
    next(csv_reader)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")

from csv import DictReader
with open ("fighter.csv") as file:
    csv_reader = DictReader(file)
    next(csv_reader)
    for fighter in csv_reader:
        print(fighter['Name'])