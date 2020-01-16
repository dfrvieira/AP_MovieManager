class Movie_Manager:
    def __init__(self):
        self.directors=[]
        self.actors=[]
        self.movies=[]
    
    def has_actor(self,name):
        for actor in self.actors:
            if actor.get_name()==name:
                return True
        return False
    
    def add_actor(self,name):
        actor=Actor(name)
        self.actors.append(actor)
    
    def has_director(self,name):
        for Director in self.directors:
            if Director.get_name()==name:
                return True
        return False

    def add_director(self,name):
        director=Director(name)
        self.directors.append(director)
    
    def has_movie(self,title,director_name):
        for movie in self.movies:
            if movie.get_title()==title and movie.get_director_name()==director_name:
                return True
        return False
    
    def change_rating(self,title,director,rating):
        for movie in self.movies:
            if movie.get_title()==title and movie.director==director:
                movie.rating=rating

    def has_movie_with_title(self,title):
        for movie in self.movies:
            if movie.title==title:
                return True
        return False

    def get_movies_by_title(self,title):
        result=[]
        for movie in self.movies:
            if movie.title==title:
                result.append(movie)
        return result

    def set_description(self,title,director,description):
        for movie in self.movies:
            if movie.title==title and movie.director==director:
                movie.description=description
                break
    
    def has_movie_with_genre(self,genre):
        for movie in self.movies:
            if movie.genre== genre:
                return True
        return False
    
    def get_movies_by_genre(self,genre):
        result=[]
        for movie in self.movies:
            if movie.genre==genre:
                result.append(movie)
        return result
    
    def has_movie_with_actor(self,actor_name):
        for movie in self.movies:
            for actor in movie.actors:
                if actor.get_name()==actor_name:
                    return True
        return False

    def get_movies_with_actor(self,actor_name):
        result=[]
        for movie in self.movies:
            for actor in movie.actors:
                if actor.get_name()==actor_name:
                    result.append(actor)
        return result
    
    def has_movie_by_director(self,director_name):
        for movie in self.movies:
            if movie.director.get_name()==director_name:
                return True
        return False

    def get_movies_with_director(self,director_name):
        result = []
        for movie in self.movies:
            if movie.director.get_name() == director_name:
                result.append(movie)
        return result
    
class Person:
    def __init__ (self,name):
        self.name = name

    def get_name(self):
        return self.name

class Actor:
    def __init__ (self,name):
        Person.__init__(self,name)

class Director:
    def __init__ (self,name):
        Person.__init__(self,name)

class Movie:
    def __init__ (self,title,Director,genre,rating):
        self.title = title
        self.director = Director
        self.genre = genre
        self.rating = rating
        self.actors = []
    
    def get_title(self):
        return self.title
    
    def get_director(self):
        return self.director
        

