file = open("tabliczka.txt", "wb")

for i in range(1, 11):
    file.write("\n")
    for j in range(1, 11):
        file.write("%4i" % (i*j),)
