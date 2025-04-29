with open('us.txt', 'r') as f:
    s = f.readlines()
    s.reverse()
    print(''.join(s))
