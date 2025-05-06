with open('input.txt', 'r') as f:
    linii = f.readlines()

with open('numbers.txt', 'w') as f:
    for linia in linii:
        if any(char.isdigit() for char in linia):
            f.write(linia)
