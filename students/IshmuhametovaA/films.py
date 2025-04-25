movies = {
    "Inception": 8.8,
    "The Dark Knight": 9.0,
    "Interstellar": 8.6,
    "Tenet": 7.5,
    "Dunkirk": 7.8
}

# 1
def add_movie(name, rating):
    if name in movies:
        print('Фильм уже существует!')
    else:
        movies[name] = rating
         print(f"Фильм '{name}' добавлен с рейтингом {rating}.")
    print(movies)

name = 'Таро: Карта смерти'
rating = 5.6
add_movie(name, rating)

#2
def find_movies(min_rating):
    print(f'Список фильмов с рейтингом выше {min_rating}:')
    for i in movies.items():
        if i[1] > min_rating:
            print(i)

find_movies(5)

#3

def average_rating():
    avg = sum(movies.values())/len(movies.values())
    print(f'Средний рейтинг всех фильмов :{avg}')

average_rating()

#4

def remove_bad_movies():
    global movies
    very_bad = []
    for i in movies.items():
        if i[1] < 6:
            very_bad.append(i[0])

    for i in very_bad:
        del movies[i]
        print(f'Удален фильм: {i}')
    print(movies)

remove_bad_movies()
