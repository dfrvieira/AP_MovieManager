import movie_manager as mml

def main():
    mm = mml.new_movie_manager()

    while True:
        line = input()
        
        commands = line.split(" ")

        if commands[0] == "RR":
            commandRR(commands, mm)
        elif commands[0] == "RA":
            commandRA(commands, mm)
        elif commands[0] == "RF":
            commandRF(commands, mm)

def commandRR(commands, mm):
    name = commands[1]
    if mml.has_director(mm, name):
        print("Realizador existente.")
    else:
        mml.add_director(mm, name)
        print("Realizador registado com sucesso.")
 
def commandRA(commands, mm):
    name = commands[1]
    if mml.has_actor(mm, name):
        print("Ator existente.")
    else:
        mml.add_ator(mm, name)
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
            mml.add_movie(mml, title, director_name)
            print("Filme adicionado com sucesso")

if __name__ == "__main__":
    main()

