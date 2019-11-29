def new_movie_manager():
    return {
        'directors': [],
        'actors': [],
        'movies': []
    }

def has_director(mm, name):
    pass

def add_director(mm, name):
    pass

def has_actor(mm, name):
    pass

def add_actor(mm, name):
    pass

def has_director(mm, name):
    for director in mm['directors']:
        for element in director:
            if director['name']==name
            return True

def add_director(mm, name):
    director = {'name': director_name}

   mm['directors'].append(director)
def has_movie(mm, title, director_name):
    pass

def add_movie(mm, title, director_name, genre,rating=None):
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

def add_actor(mm,name):
    actor = {'name':actor_name}

    mm['actors'].append(actor)

def has_movie_with_title(mm, title):
    for movie in mm['movies']:
        for element in movie:
            if movie['title']==title:
                return True

def get_movies_by_title(mm, title):
    for movie in mm['movies']:
        for element in movie:
            if movie['title']==title:
                output=str(movie.values())
                return output[-13:-2] #removes the unwanted text from the output
def set_description(mm, title, director_name, description):
    pass

