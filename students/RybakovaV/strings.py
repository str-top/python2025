#1
abs = 'Код, который переобразует строку из десяти слов в верхний регистр'
print(abs.upper())
print(abs.count("а"))
print(abs.replace(" ", "-"))
#2
sba = 'Код, который переобразует строку из десяти слов в верхний регистр'
print(sba.split(" "))
#3
proposal = "я делаю курсы"
if not proposal[0].isupper():
        proposal = proposal[0].upper() + proposal[1:]
if not proposal[-1] in ['.', '!', '?']:
        proposal += '.'
print(proposal)
