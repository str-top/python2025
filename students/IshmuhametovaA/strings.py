1) text = "Это пример строки из десяти слов для демонстрации работы кода"

upper_text = text.upper()
print("Верхний регистр:", upper_text)

count_a = text.lower().count('а')
print("Количество букв 'а':", count_a)

dash_text = text.replace(' ', '-')
print("С заменой пробелов:", dash_text)
2) words = text.split()
print("\nОтдельные слова:")
for word in words:
    print(word)
3) def fix_sentence(sentence):
    if len(sentence) > 0 and not sentence[0].isupper():
        sentence = sentence[0].upper() + sentence[1:]
    if len(sentence) > 0 and sentence[-1] not in {'.', '!', '?', ';', ':'}:
        sentence += '.'
    
    return sentence

test_sentences = [
    "это тестовое предложение",
    "Это предложение без точки",
    "корректное предложение."
]

print("\nПроверка предложений:")
for sent in test_sentences:
    fixed = fix_sentence(sent)
    print(f"До: '{sent}' -> После: '{fixed}'")
