movies = {
    "Inception": 8.8,
    "The Dark Knight": 9.0,
    "Interstellar": 8.6,
    "Tenet": 7.5,
    "Dunkirk": 7.8
}

def add_movie(name, rating):
    if name in movies:
        print("Фильм уже существует!")
    else:
        movies[name] = rating
        print(f"Фильм '{name}' с рейтингом {rating} добавлен.")

def find_movies(min_rating):
  return [movie for movie, rating in movies.items() if rating >= min_rating]
  
def  average_rating():
    if not movies:
        return 0.0
    return sum(movies.values()) / len(movies)
    
def remove_bad_movies():
    bad_movies = [movie for movie, rating in movies.items() if rating < 6.0]
    for movie in bad_movies:
        del movies[movie]
    print(f"Удалено {len(bad_movies)} фильмов.")
    
if __name__ == "__main__":
    print("Исходный список фильмов:", movies)
    add_movie("The Prestige", 2.5)
    add_movie("Inception", 9.0)
    print("После добавления:", movies)
    print("Фильмы с рейтингом >= 7.0:", find_movies(7.0))
    print("Средний рейтинг:", average_rating())
    remove_bad_movies()
    print("После удаления плохих фильмов:", movies)
    
