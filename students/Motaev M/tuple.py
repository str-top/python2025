with open('file.txt', 'w') as f:
    f.write('abcde')

with open("file.txt") as f:
    content = f.read()
    print(content[::-1])