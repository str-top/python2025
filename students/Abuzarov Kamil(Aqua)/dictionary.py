class LimitedDictionary:
    def __init__(self):
        self.dictionary = {}
        self.max_size = 10

    def add_word(self, word, meaning):
        if len(self.dictionary) >= self.max_size:
            print("Словарь полон! Невозможно добавить новое слово.")
            return
        if word in self.dictionary:
            print(f"Слово '{word}' уже есть в словаре. Используйте функцию обновления.")
            return
        self.dictionary[word] = meaning
        print(f"Слово '{word}' успешно добавлено.")

    def get_meaning(self, word):
        if word in self.dictionary:
            return self.dictionary[word]
        else:
            return f"Слово '{word}' не найдено в словаре."

    def delete_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]
            print(f"Слово '{word}' успешно удалено.")
        else:
            print(f"Слово '{word}' не найдено в словаре.")

    def display_dictionary(self):
        print("Текущий словарь:")
        for word, meaning in self.dictionary.items():
            print(f"{word}: {meaning}")


# Пример использования
dict_10 = LimitedDictionary()

# Добавление слов
dict_10.add_word("apple", "яблоко")
dict_10.add_word("book", "книга")
dict_10.add_word("cat", "кошка")
dict_10.add_word("dog", "собака")
dict_10.add_word("house", "дом")
dict_10.add_word("tree", "дерево")
dict_10.add_word("water", "вода")
dict_10.add_word("sun", "солнце")
dict_10.add_word("moon", "луна")
dict_10.add_word("star", "звезда")

# Попытка добавить 11-е слово
dict_10.add_word("car", "машина")  # Должно вывести сообщение о переполнении

# Вывод значений
print(dict_10.get_meaning("book"))  # книга
print(dict_10.get_meaning("car"))   # Сообщение об отсутствии

# Удаление слова
dict_10.delete_word("cat")
dict_10.delete_word("fish")  # Сообщение об отсутствии

# Вывод всего словаря
dict_10.display_dictionary()
