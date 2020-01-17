class Person:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class Actor(Person):
    def __init__(self, actor_name):
        Person.__init__(self, actor_name)

class Director(Person):
    def __init__(self, directo_name):
        Person.__init__(self, director_name)

class Movie:
    pass

class MovieManager:
    def __init__(self):
        self.directors = []
        self.actors = []
        self.movies = []
    
    def has_director(self, director_name):
        for director in self.directors:
            if director.get_name() == name:
                return True
        return False
    
    def add_director(self, director_name):
        # director = {'name': name}
        # mm['directors'].append(director)
        director = Director(director_name)
        self.directors.append(director)
