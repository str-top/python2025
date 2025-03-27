
def string_operations(text):

    upper_text = text.upper()
    print(f"Строка в верхнем регистре: {upper_text}")

    count_a = text.lower().count('а')
    print(f"Количество букв 'а' (без учета регистра): {count_a}")

    replaced_text = text.replace(" ", "-")
    print(f"Строка с замененными пробелами: {replaced_text}")

def split_string(text):

    words = text.split()
    print("Слова в строке:")
    for word in words:
        print(word)

def validate_and_correct_sentence(sentence):

    original_sentence = sentence

    if not sentence:
        return "Предложение пустое."
    
    if not sentence[0].isupper():
        sentence = sentence[0].upper() + sentence[1:]

    punctuation_marks = ['.', '?', '!']
    if sentence[-1] not in punctuation_marks:
        sentence += '.'

    if original_sentence == sentence:
        print("Предложение корректно")
    else:
        print("Предложение было исправлено")
    return sentence

ten_word_string = "Это строка в которой должно находиться десять слов антилопа яблоко" 
string_operations(ten_word_string)

print("\n--- Разделение строки на слова ---")
split_string("Это строка в которой слова должны разбиваться на строки")

print("\n--- Проверка и исправление предложений ---")
sentence1 = "привет мир"
corrected_sentence1 = validate_and_correct_sentence(sentence1)
print(f"Исходное предложение: hello world\nИсправленное предложение: {corrected_sentence1}")

sentence2 = "Привет мир"
corrected_sentence2 = validate_and_correct_sentence(sentence2)
print(f"\nИсходное предложение: Hello world\nИсправленное предложение: {corrected_sentence2}")

sentence3 = "Привет мир."
corrected_sentence3 = validate_and_correct_sentence(sentence3)
print(f"\nИсходное предложение: Hello world.\nИсправленное предложение: {corrected_sentence3}")

sentence4 = "так корректно?"
corrected_sentence4 = validate_and_correct_sentence(sentence4)
print(f"\nИсходное предложение: is this correct?\nИсправленное предложение: {corrected_sentence4}")

sentence5 = ""
corrected_sentence5 = validate_and_correct_sentence(sentence5)
print(f"\nИсходное предложение: (пустое)\nИсправленное предложение: {corrected_sentence5}")
