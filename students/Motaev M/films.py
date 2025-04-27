movies = {
    "Inception": 8.8,
    "The Dark Knight": 9.0,
    "Interstellar": 8.6,
    "Tenet": 7.5,
    "Dunkirk": 7.8
}
    
def add():
    name = input('введите название фильма: ')
    if name in movies:
        print("фильм уже существует!")
    else:
        rating = float(input(f'введите рейтинг фильма {name}: '))
        movies[name] = rating
        print(f"фильм '{name}' добавлен с рейтингом {rating}.")
    
def poisk():
    min_rating = float(input('Введите минимальный рейтинг: '))
    found_movies = [name for name, rating in movies.items() if rating >= min_rating]
    print("найденные фильмы:", found_movies)
    
def avg_rate():
    if not movies:
        return 0
    avg = sum(movies.values()) / len(movies)
    print(f"средний рейтинг всех фильмов: {avg:.2f}")
    
def delete():
    global movies
    movies = {name: rating for name, rating in movies.items() if rating >= 6.0}
    print("плохие фильмы удалены.")

while True:    
    menu = """
Выберите действие:
1 - добавить фильм
2 - поиск по рейтингу
3 - средний рейтинг списка
4 - удалить фильмы с рейтингом ниже 6
    """
    
    vibor = input(menu)
    
    if vibor == '1':
        add()
    elif vibor == '2':
        poisk()
    elif vibor == '3':
        avg_rate()
    elif vibor == '4':
        delete()
    else:
        print('неверная команда')
