from random import randint
N_computador = randint(1,10)
Tipo = " "
total = 0


while True:
    print("-=-"*10)
    print("Vamos jogar Par ou ímpar")
    print("-=-"*10)
    Tipo = str(input("Par ou Ímpar? ")).strip().upper()[0]
    N = int(input("Jogue seu número: "))
    total = N_computador + N
    while Tipo == "P":
        if total % 2 == 0: #par
        
            
        else:# Impar
            break
