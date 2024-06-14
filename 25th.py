#copy one file to another

with open("divya.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)
f.close()
f1.close()