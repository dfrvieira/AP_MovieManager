def new_movie_manager():
    return {
        'directors': [],
        'actors': [],
        'movies': []
    }


def has_actor(mm, name):
    for actor in mm['actors']:
        if actor['name']==name:
            return True
    return False

def add_actor(mm,name):
    actor = {'name':actor_name}

    mm['actors'].append(actor)


def has_director(mm, name):
    for director in mm['directors']:
        for element in director:
            if director['name']==name:
                return True
    return False

def add_director(mm, name):
    director = {'name': director_name}

   mm['directors'].append(director)

def has_movie(mm, title, director_name):
    for movie in mm['movies']:
        for element in movie:
            if movie['title']==title and movie['director']==director_name:
                return True
    return False

def add_movie(mm, title, director_name, genre,rating='Por classificar'):
    movie = {
            'title':title,
            'director':director_name,
            'genre':genre
            'rating':rating
            }
    mm['movies'].append(movie)

def change_rating(mm, title, director_name, rating):
    for movie in mm['movies']:
        for element in movie:
            if movie['title']==title and movie['director']==director_name:
                movie['rating']=rating

def has_movie_with_title(mm, title):
    for movie in mm['movies']:
        for element in movie:
            if movie['title']==title:
                return True
    return False

def get_movies_by_title(mm, title):
    for movie in mm['movies']:
        for element in movie:
            if movie['title']==title:
                output=str(movie.values())
                return output[-13:-2] #removes the unwanted text from the output

def set_description(mm, title, director_name, description):
    for movie in mm['movies']:
        for element in movie :
            if movie['title']==title and movie ['director']==director_name:
                movie['description']= description

