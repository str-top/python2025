##task 1
sdfeas= 'Высыпать, Головомойка, Жердь, Инородный, Козел, Наерундить, Переулок, Повседневность, Почтенный, Фрамуга'
print(sdfeas.upper())
print(sdfeas.count("а"))
print(sdfeas.replace(" ", "-"))
## task 2
aaa= 'Высыпать, Головомойка, Жердь, Инородный, Козел, Наерундить, Переулок, Повседневность, Почтенный, Фрамуга'
print(aaa.split(" "))
##task 3
sentence = "z хочу спать"
if not sentence[0].isupper():
        sentence = sentence[0].upper() + sentence[1:]
    
    # Проверяем, что в конце предложения стоит знак препинания
if not sentence[-1] in ['.', '!', '?']:
        sentence += '.'
print(sentence)
    
