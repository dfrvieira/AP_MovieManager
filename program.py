import movie_manager as m_m

def main():
    mm = m_m.MovieManager()
    while True:
        line = input()
        if not line:      # checks if input is empty line , if so
            break         # it breaks out of while loop
        commands = line.split(" ")

        if commands[0] == "RR":
            commandRR(commands, mm)
        elif commands[0] == "RA":
            commandRA(commands, mm)
        elif commands[0] == "RF":
            commandRF(commands, mm)
        elif commands[0] == "AA":
            commandAA(commands, mm)
        elif commands[0] == "AR":
            commandAR(commands, mm)
        elif commands[0] == "AS":
            commandAS(commands, mm)
        elif commands[0] == "PT":
            commandPT(commands, mm)
        elif commands[0] == "PG":
            commandPG(commands, mm)
        elif commands[0] == "PA":
            commandPA(commands, mm)
        elif commands[0] == "PR":
            commandPR(commands, mm)
        else:
            print("Instrução inválida.")

def commandRR(commands, mm):
    director_name = commands[1]
    if mm.has_director(director_name):
        print("Realizador existente.")
    else:
        mm.add_director(director_name)
        print("Realizador registado com sucesso.")

def commandRA(commands, mm):
    actor_name = commands[1]
    if mm.has_actor(actor_name):
        print("Ator existente.")
    else:
        mm.add_actor(actor_name)
        print("Ator registado com sucesso.")

def commandRF(commands, mm):
    title = commands[1]
    director_name = commands[2]
    genre = commands[3]

    if not mm.has_director(director_name):
        print("Realizador inexistente.")
    else:
        if mm.has_movie(title,director_name):
            print("Filme existente.")
        else:
            filme = m_m.Movie(title, director_name, genre)
            mm.add_movie(filme)
            print("Filme adicionado com sucesso")

def commandAA(commands,mm):
    title = commands[1]
    director_name = commands[2]
    actor_name = commands[3]

    if not mm.has_director(director_name):
        print("Realizador inexistente")
    else:
        if not mm.has_movie(title, director_name):
            print("Filme inexistente")
        else:
            if not mm.has_actor(actor_name):
                print("Actor inexistente")
            else:
                mm.add_actor_to_movie(actor_name, title, director_name)
                print("Ator adicionado com sucesso")

def commandAR(commands, mm):
    title = commands[1]
    director_name = commands[2]
    rating = commands[3]
    if not mm.has_director(director_name):
        print("Realizador inexistente.")
    elif not mm.has_movie(title, director_name):
        print("Filme inexistente.")
    else:
        mm.change_rating(title, director_name, rating)
        print("Rating alterado com sucesso.")

def commandAS(commands, mm):
    title = commands[1]
    director_name = commands[2]
    description = input('Sinopse: ')
    if not mm.has_director(director_name):
        print("Realizador inexistente.")
    if not mm.has_movie(title, director_name):
        print("Filme inexistente.")
    else:
        mm.set_description(title, director_name, description)
        print("Sinopse alterada com sucesso.")

def commandPT(commands, mm):
    title = commands[1]
    if not mm.has_movies():
        print("Sem filmes registados.")
    elif not mm.has_movie_with_title(title):
        print("Sem resultados.")
    else:
        movies = mm.get_movies_by_title(title)
        for movie in movies:
            director_name = movie.get_director()
            print(f"{director_name} {title}")

def commandPG(commands, mm):
    genre = commands[1]
    if not mm.has_movies():
        print("Sem filmes registados.")
    elif not mm.has_movie_with_genre(genre):
        print("Sem resultados.")
    else:
        movies = mm.get_movies_by_genre(genre)
        for movie in movies:
            director_name = movie.get_director()
            title = movie.get_titulo()
            print(f"{director_name} {title}")

def commandPA(commands, mm):
    actor_name = commands[1]
    if not mm.has_movies():
        print ("Sem filmes registados")
    elif not mm.has_actor(actor_name):
        print("Ator inexistente")
    elif not mm.has_movie_with_actor(actor_name):
        print("Sem resultados")
    else:
        movies = mm.get_movies_with_actor(actor_name)
        for movie in movies:
            director_name = movie.get_director()
            title = movie.get_titulo()
            print(f"{director_name} {title}")

def commandPR(commands, mm):
    director_name = commands[1]
    if not mm.has_movies():
        print ("Sem filmes registados")
    elif not mm.has_director(director_name):
        print("Realizador inexistente")
    elif not mm.has_movie_by_director(director_name):
        print("Sem resultados")
    else:
        movies = mm.get_movies_by_director(director_name)
        for movie in movies:
            director_name = movie.get_director()
            title = movie.get_titulo()
            print(f"{director_name} {title}")

if __name__ == "__main__":
    main()


