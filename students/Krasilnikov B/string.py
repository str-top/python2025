first_row = 'Это первая строка которую нужно отформатировать с помощью кода Python.'

# First_Task
bigger_letters = first_row.upper()
print(bigger_letters)
print(first_row.count('а'))
print(bigger_letters.replace(' ', '-'))

# Second_Task

words = first_row.split(' ')

for word in words:
    print(word)

# Third_Task

print(first_row.startswith('Э'))
print(first_row.endswith('.'))
