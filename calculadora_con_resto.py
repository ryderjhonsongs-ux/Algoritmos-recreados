
while True:
    eqa = int(input("NUMERO 1 :: > "))
    eqb = int(input("NUMERO 2 :: > "))

    res = eqa // eqb

    resto = eqa % eqb

    print(f"Resultado: {res} y Resto: {resto} ")

    ppp = input("Pulsa enter para continuar y X para cerrar:...: ")

    if ppp == "x".lower():

        break

    else:

        print()
