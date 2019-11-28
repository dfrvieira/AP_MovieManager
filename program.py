import movie_manager as mml

def main():
    mm = mml.new_movie_manager()

    while True:
        line = input()

        if line == '':    #checks if input is empty line , if so
            break         #it breaks out of while loop

        commands = line.split(" ")

        if commands[0] == "RR":
            commandRR(commands, mm)

        if commands[0]=="RA":
            commandRA(commands, mm)

        if commands[0]=="RF":
            commandRF(commands, mm)

        if commands[0]=="AA":
            commandAA(commands, mm)

    def commandRR(commands, mm):

         name = commands[1]
         if mml.has_director(mm, name):
             print("Realizador existente.")
         else:
             mml.add_director(mm, name)
             print("Realizador registado com sucesso.")

    def commandRA(commands,mm):
        name =  commands[1]
        if mml.has_actor(mm,name):
            print("Actor existente")
        else:
            mm.add_Actor(mm,name)
            print("Ator registado com sucesso.")

    def commandRF(commands,mm):
       title = commands[1]
       director = commands[2]
       genre = commands[3]
       if mm.has_movie(mm,title):
           print("Filme existente")
       elif 1==1: #realiador in Lista de Realizadores:
            print("Realizador inexistente")
       else:
           mm.add_filme(mm, title, director, genre)
           print("Filme adcionado com sucesso")

    def commandAA(commands, mm):
        pass


if __name__ == "__main__":
    main()
