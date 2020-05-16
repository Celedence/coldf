from csv import writer

with open("cats.csv", "w") as file:
    cat_file = writer(file)
    cat_file.writerow(["Name", "Age"])
    cat_file.writerow(["Annabelle", 5])
    cat_file.writerow(["Nubs", 1])