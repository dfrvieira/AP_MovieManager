import movie_manager as mm

def main():
    movie_manager_D = {}
    while True:
        line = input()
        
        commands = line.split(" ")

        if commands[0] == "RR":
            commandRR(commands, movie_manager_D)

def commandRR(commands, movie_manager_D):
    name = commands[1]
    if mm.has_director(movie_manager_D, name):
        print("Realizador existente.")
    else:
        mm.add_director(movie_manager_D, name)
        print("Realizador registado com sucesso.")

if __name__ == "__main__":
    main()

