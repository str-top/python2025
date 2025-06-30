movies = {
    "Inception": 8.8,
    "The Dark Knight": 9.0,
    "Interstellar": 8.6,
    "Tenet": 7.5,
    "Dunkirk": 7.8
}

def add_movie():
    name = input("Введите название фильма: ")
    while True:
        try:
            rating = float(input("Введите рейтинг фильма (0-10): "))
            if 0 <= rating <= 10:
                break
            else:
                print("Рейтинг должен быть от 0 до 10!")
        except ValueError:
            print("Пожалуйста, введите число!")
    
    movies[name] = rating
    print(f"Фильм '{name}' с рейтингом {rating} добавлен в список!")
    print_current_movies()

def find_movies():
    while True:
        try:
            min_rating = float(input("Введите минимальный рейтинг (0-10): "))
            if 0 <= min_rating <= 10:
                break
            else:
                print("Рейтинг должен быть от 0 до 10!")
        except ValueError:
            print("Пожалуйста, введите число!")
    
    found_movies = {}
    for name, rating in movies.items():
        if rating >= min_rating:
            found_movies[name] = rating
    
    if found_movies:
        print(f"\nФильмы с рейтингом {min_rating} и выше:")
        for name, rating in found_movies.items():
            print(f"- {name}: {rating}")
    else:
        print("Нет фильмов с таким рейтингом")
    print_current_movies()

def average_rating():
    if not movies:
        print("Список фильмов пуст!")
        return
    
    avg = sum(movies.values()) / len(movies)
    print(f"Средний рейтинг всех фильмов: {avg:.1f}")
    print_current_movies()

def remove_bad_movies():
    bad_movies = []
    for name, rating in movies.items():
        if rating < 6.0:
            bad_movies.append(name)
    
    if not bad_movies:
        print("Нет фильмов с рейтингом ниже 6.0")
    else:
        for name in bad_movies:
            del movies[name]
        print(f"Удалены фильмы: {', '.join(bad_movies)}")
    print_current_movies()

def print_current_movies():
    print("\nТекущий список фильмов:")
    if movies:
        for name, rating in movies.items():
            print(f"- {name}: {rating}")
    else:
        print("Список пуст")
    print()

while True:
    menu = """
Введите операцию:
1 - Добавление фильма
2 - Поиск фильма по рейтингу
3 - Средний рейтинг всех фильмов
4 - Удаление фильмов с низким рейтингом
5 - Выход
Выбор: """
    
    choice = input(menu).strip()
    
    if choice == '1':
        add_movie()
    elif choice == '2':
        find_movies()
    elif choice == '3':
        average_rating()
    elif choice == '4':
        remove_bad_movies()
    elif choice == '5':
        print("Выход из программы...")
        break
    else:
        print("Неверный выбор операции. Пожалуйста, введите число от 1 до 5")
