movies = {
    "Inception": 8.8,
    "The Dark Knight": 9.0,
    "Interstellar": 8.6,
    "Tenet": 7.5,
    "Dunkirk": 7.8
}
def add_movie(name, rating):
    global movies
    movies[name] = rating

add_movie("Lock, Stock and Two Smoking Barrels", 8.6)
add_movie("Bucky Larson: Born to Be a Star", 3.0)

user_input = input("Введите рейтинг: ")
min_rating = float(user_input) 

def find_movies(min_rating): # не понл как сделать сделал с помощью чатгпт(
    found_movies = []
    for movie, rating in movies.items():
        if rating >= min_rating:
            found_movies.append(movie)
    return found_movies
result = find_movies(min_rating)

if result:
    print(f"Фильмы с рейтингом не ниже {min_rating}: {result}")
else:
    print(f"Нет фильмов с рейтингом не ниже {min_rating}.")
    
def average_rating():
    total_rating = 0
    for rating in movies.values():
        total_rating += rating
avg_rating = average_rating()
print(f"Средний рейтинг фильмов: {average_rating}")

def remove_bad_movies():
    global movies
    bad_movies = [movie for movie, rating in movies.items() if rating < 6.0]
    for movie in bad_movies:
        del movies[movie]

remove_bad_movies()
    
print(movies)
