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
    for row in csv_reader:
        print(row)

