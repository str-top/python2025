cities_list = []

def add_city(city):
    cities_list.append(city)

def sort_by_length():
    cities_list.sort(key=lambda x: len(x))

def remove_city(city):
    if city in cities_list:
        cities_list.remove(city)

# Пример использования:
add_city("Москва")
add_city("Санкт-Петербург")
add_city("Казань")
sort_by_length()
print(cities_list)  # ['Казань', 'Москва', 'Санкт-Петербург']
remove_city("Москва")
print(cities_list)  # ['Казань', 'Санкт-Петербург']


cities_set = set()

def add_city(city):
    cities_set.add(city)

def sort_by_length():
    return sorted(cities_set, key=lambda x: len(x))

def remove_city(city):
    cities_set.discard(city)

# Пример использования:
add_city("Москва")
add_city("Санкт-Петербург")
add_city("Казань")
print(sort_by_length())  # ['Казань', 'Москва', 'Санкт-Петербург']
remove_city("Москва")
print(cities_set)  # {'Казань', 'Санкт-Петербург'}


cities_dict = {}

def add_city(city):
    cities_dict[city] = len(city)

def sort_by_length():
    return sorted(cities_dict.keys(), key=lambda x: len(x))

def remove_city(city):
    cities_dict.pop(city, None)

# Пример использования:
add_city("Москва")
add_city("Санкт-Петербург")
add_city("Казань")
print(sort_by_length())  # ['Казань', 'Москва', 'Санкт-Петербург']
remove_city("Москва")
print(cities_dict)  # {'Санкт-Петербург': 15, 'Казань': 6}


from collections import deque

cities_deque = deque()

def add_city(city):
    cities_deque.append(city)

def sort_by_length():
    global cities_deque
    cities_deque = deque(sorted(cities_deque, key=lambda x: len(x)))

def remove_city(city):
    if city in cities_deque:
        cities_deque.remove(city)

# Пример использования:
add_city("Москва")
add_city("Санкт-Петербург")
add_city("Казань")
sort_by_length()
print(cities_deque)  # deque(['Казань', 'Москва', 'Санкт-Петербург'])
remove_city("Москва")
print(cities_deque)  # deque(['Казань', 'Санкт-Петербург'])




