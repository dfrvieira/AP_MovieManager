def new_movie_manager():
    return {
        'directors': [],
        'actors': [],
        'movies': []
    }

def has_actor(mm, name):
    for actor in mm['actors']:
        if actor['name'] == name:
            return True
    return False

def add_actor(mm,name):
    actor = {
        'name': name
    }
    mm['actors'].append(actor)

def has_director(mm, name):
    for director in mm['directors']:
        if director['name'] == name:
            return True
    return False

def get_director(mm, name):
    for director in mm['directors']:
        if director['name'] == name:
            return director
    return None

def add_director(mm, name):
    director = {
        'name': name
    }
    mm['directors'].append(director)

def has_movie(mm, title, director_name):
    for movie in mm['movies']:
        if movie['title'] == title and movie['director'] == director_name:
            return True
    return False

def add_movie(mm, title, director_name, genre, rating=0.0):
    director = get_director(mm, director_name)
    movie = {
        'title': title,
        'director': director,
        'genre': genre,
        'rating': rating
    }
    mm['movies'].append(movie)

def change_rating(mm, title, director_name, rating):
    for movie in mm['movies']:
        if movie['title'] == title and movie['director'] == director_name:
            movie['rating'] = rating
            break

def has_movie_with_title(mm, title):
    for movie in mm['movies']:
        if movie['title'] == title:
            return True
    return False

def get_movies_by_title(mm, title):
    result = []
    for movie in mm['movies']:
        if movie['title'] == title:
            result.append(movie)
    return result

def set_description(mm, title, director_name, description):
    for movie in mm['movies']:
        if movie['title'] == title and movie['director'] == director_name:
            movie['description'] = description
            break

def has_movie_with_genre(mm, genre):
    for movie in mm['movie']:
        if movie['genre'] == genre:
            return True
    return False

def get_movies_by_genre(mm, genre):
    result = []
    for movie in mm['movie']:
        if movie['genre'] == genre:
            result.append(movie)
    return result

def has_movie_with_actor(mm, actor_name):
    pass

def get_movies_with_actor(mm, actor_name):
    pass

def has_movie_by_director(mm, director_name):
    pass

def get_movies_by_director(mm, director_name):
    pass
