with open('input.txt', 'r') as f:
    new = open("numbers.txt", "w")
    for line in f:
        res = any(char.isdigit() for char in line)
        if res:
            new.write(line)
            print(line)
    
