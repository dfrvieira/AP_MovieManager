class Movie_Manager:
    def __init__(self):
        self.directors=[]
        self.actors=[]
        self.movies=[]
    
    def has_actor(self,name):
        for Actor in self.actors:
            if Actor.get_name==name:
                return True
        return False
    
    def add_actor(self,name):
        actor=Actor(name)
        self.actors.append(actor)
    
    def has_director(self,name):
        for Director in self.directors:
            if Director.get_name==name:
                return True
        return False

    def add_director(self,name):
        director=Director(name)
        self.directors.append(director)
    
    def get_director(self,name):
        for Director in self.directors:
            if Director.get_name==name:
                return Director

    def has_movie(self,title,director_name):
        for Moive in self.movies:
            if Movie.get_title==title and Movie.get_director_name==director_name:
                return True
        return False
class Person:
    def __init__ (self,name):
        self.name=name

    def get_name(self):
        return self.name

class Actor:
    def __init__ (self,name):
        Person.__init__(self,name)

class Director:
    def __init__ (self,name):
        Person.__init__(self,name)

class Movie:
    def __init__ (self,title,director,genre,rating):
        self.title=title
        self.director_name= Movie_Manager.get_director(director)
        self.genre=genre
        self.rating=rating
        self.actors=[]
    
    def get_title(self):
        return self.title
    
    def get_director_name(self):
        return self.director_name
        

