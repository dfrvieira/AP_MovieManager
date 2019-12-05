import movie_manager as mml

def main():
    mm = mml.new_movie_manager()
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
    if mml.has_director(mm, director_name):
        print("Realizador existente.")
    else:
        mml.add_director(mm, director_name)
        print("Realizador registado com sucesso.")

def commandRA(commands, mm):
    actor_name = commands[1]
    if mml.has_actor(mm, actor_name):
        print("Ator existente.")
    else:
        mml.add_actor(mm, actor_name)
        print("Ator registado com sucesso.")

def commandRF(commands, mm):
    title = commands[1]
    director_name = commands[2]
    genre = commands[3]

    if not mml.has_director(mm, director_name):
        print("Realizador inexistente.")
    else:
        if mml.has_movie(mm, title, director_name):
            print("Filme existente.")
        else:
            mml.add_movie(mm, title, director_name, genre)
            print("Filme adicionado com sucesso")

def commandAA(commands, mm):
    title = commands[1]
    director_name = commands[2]
    actor_name = commands[3]
    if not mml.has_director(mm, director_name):
        print("Realizador inexistente")
    else:
        if not mml.has_movie(mm, director_name, title):
            print("Filme inexistente")
        else:
            if not mml.has_actor(mm, director_name, title, actor_name):
                print("Actor inexistente")
            else:
                mml.add_actor_to_movie(mm, actor_name, title, director_name)
                print("Ator adicionado com sucesso")

def commandAR(commands, mm):
    title = commands[1]
    director_name = commands[2]
    rating = commands[3]
    if not mml.has_director(mm, director_name):
        print("Realizador inexistente.")
    elif not mml.has_movie(mm, title, director_name):
        print("Filme inexistente.")
    else:
        mml.change_rating(mm, director_name, title, rating)
        print("Rating alterado com sucesso.")

def commandAS(commands, mm):
    title = commands[1]
    director_name = commands[2]
    description = input()
    if not mml.has_director(mm, director_name):
        print("Realizador inexistente.")
    if not mml.has_movie(mm, title, director_name):
        print("Filme inexistente.")
    else:
        mml.set_description(mm, title, director_name, description)
        print("Sinopse alterada com sucesso.")

def commandPT(commands, mm):
    title = commands[1]
    if not mml.has_movies(mm):
        print("Sem filmes registados.")
    elif not mml.has_movie_with_title(mm, title):
        print("Sem resultados.")
    else: 
        movies = mml.get_movies_by_title(mm, title)
        for movie in movies:
            director_name = movie['director']['name']
            print(f"{director_name} {title}")

def commandPG(commands, mm):
    genre = commands[1]
    if not mml.has_movies(mm):
        print("Sem filmes registados.")
    elif not mml.has_movie_with_genre(mm, genre):
        print("Sem resultados.")
    else:
        movies = mml.get_movies_by_genre(mm, genre)
        for movie in movies:
            director_name = movie['director']['name']
            title = movie['title']
            print(f"{director_name} {title}")

def commandPA(commands, mm):
    actor_name = commands[1]
    if not mml.has_movies(mm):
        print ("Sem filmes registados")
    elif not mml.has_actor(mm, actor_name):
        print("Ator inexistente")
    elif not mml.has_movie_with_actor(mm, actor_name):
        print("Sem resultados")
    else:
        movies = mml.get_movies_with_actor(mm, actor_name)
        for movie in movies:
            director_name =['director']['name']
            title = movie['title']
            print(f"{director_name} {title}")

def commandPR(commands, mm):
    director_name = commands[1]
    if not mml.has_movies(mm):
        print ("Sem filmes registados")
    elif not mml.has_director(mm, director_name):
        print("Realizador inexistente")
    elif not mml.has_movie_by_director(mm, director_name):
        print("Sem resultados")
    else:
        movies = mml.get_movies_by_director(mm, director_name)
        for movie in movies:
            director_name =['director']['name']
            title = movie['title']
            print(f"{director_name} {title}")

if __name__ == "__main__":
    main()


