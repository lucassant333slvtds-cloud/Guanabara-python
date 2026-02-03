resp = "S"
while resp in 'Ss':
    n = int(input("Digite um número: "))
    resp = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
print("cabo!")
