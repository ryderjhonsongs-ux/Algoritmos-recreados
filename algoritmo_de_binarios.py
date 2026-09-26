bit = input("Tu Bin aca: ")

lan = len(bit)

if lan < 8:
    print("Debe ser un byte completo de 8 caracteres")

elif not all(c in "01" for c in bit):
    print("Solo se aceptan binarios 1 y 0")

else:
    result = 0
    pesos = [128, 64, 32, 16, 8, 4, 2, 1]

    for i in range(8):
        if bit[i] == "1":
            result += pesos[i]

    print(f"Decimal: {result}")
