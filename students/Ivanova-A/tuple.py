d = open("input.txt", 'r')
f = open("numbers.txt", "w+")
for line in d:
        if any (char.isdigit() for char in line):
            f.write(line)
            print(f.read())
f.close()
d.close()
