np = int(input("Num1:: >> "))
resta = np
res = np

for i in range(np):

    resta -= 1

    if resta == 0:
        break

    print(f"{res} x {resta} = {res * resta}")

    res *= resta
