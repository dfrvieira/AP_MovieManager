class Movie:
    def __init__(self, titulo, director, genre, ratting=None, description=None):
        self.titulo = titulo
        self.director= director
        self.genre = genre
        self.ratting = ratting
        self.actors = []
        self.description = description

    def get_titulo(self):
        return self.titulo

    def get_ratting(self):
        return self.ratting

    def get_genre(self):
        return self.genre

    def get_description(self):
        return self.description

    def get_director(self):
        return self.director

    def get_actors(self):
        return self.actors #returns a list

    def set_actor(self, actor):
        self.actors.append(actor)

    def set_description(self,description):
        self.description = description

    def set_ratting(self,ratting):
        self.ratting = ratting

    def add_actor(self,actor):
        self.actors.append(actor)

class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Actor(Person):
    def __init__(self,name):
        Person.__init__(self, name)

class Director(Person):
    def __init__(self,name):
        Person.__init__(self, name)

class MovieManager:
    def __init__(self):
        self.movies = []
        self.actors = []
        self.directors = []

    def has_director(self, director_name):
        for director in self.directors:
            if director.get_name() == director_name:
                return True
    
    def get_directors(self):
        return self.directors

    def has_actor(self, actor_name):
        for actor in self.actors:
            if actor.get_name() == actor_name:
                return True

    def add_movie(self,movie):
        self.movies.append(movie)

    def has_movie(self,movie_titulo):
        for movie in self.movies:
            if movie.get_titulo == movie_titulo:
                return True

    def get_actor(self,name):
        for actor in self.actors:
            if actor.name == name:
                return actor

    def get_movie_by_genre(self,genre):
        movie_list=[]
        for movie in self.movies:
            if movie.get_genre() == genre:
                movie_list.append(movie)

    def add_actor(self, actor_name):
        actor = Actor(actor_name)
        self.actors.append(actor)

    def add_director(self, director_name):
        director = Director(director_name)
        self.directors.append(director)

    def get_movie(self,movie_title):
        for movie in self.movies:
            if movie.titulo == movie_title:
                return movie

    def add_actor_to_movie(self, actor_name, movie_title):
        actor = self.get_actor(actor_name)
        movie = self.get_movie(movie_title)
        movie.add_actor(actor)

    def has_movie_with_actor(self,actor_name):
        for movie in self.movies:
            for actor in movie.get_actors():
                if actor_name in actor:
                    return movie.titulo

