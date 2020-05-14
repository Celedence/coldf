# with open("newer.txt", "w") as file:
#     file.write("overwriting line of text\n")
#     file.write("this is a new line\n")
#     file.write("this has been atered")

# with open ("newer.txt", "w") as file:
#     file.write("hahah" * 10000)

with open ("newer.txt", "a") as file:
    file.write(" this will be appended later")