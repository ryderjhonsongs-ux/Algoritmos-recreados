import random


try:

    while True:
        for i in range(8):

            print(random.randint(0,1), end="")

        put = input("\nPRESIONE ENTER PARA CONTINUAR O X PARA CERRAR: ")

        if put.lower() == "x":
            break
except KeyboardInterrupt, EOFError:

    print()
