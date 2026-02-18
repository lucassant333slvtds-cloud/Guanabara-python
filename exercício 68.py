from random import randint
from time import sleep
N_usuario = computador = cont = total = comparador = resultado = 0 
P_I = " "
vitoria = 0 
total = computador + N_usuario
print("P A R    O U    I M P A R ")




while True:
    N_usuario = int(input("Dgigite um valor entre 1 e 10: "))
    computador = randint(0,10)
    total = N_usuario + computador
    
    while P_I not in "PI": #par ou impar
        P_I = str(input("Par ou impar? (P/I) ")).strip()[0]
    print(f"Vc jogou {N_usuario} e o computaodr jogou {computador}. Total de {total}")

    if P_I == "P":
        if total % 2 == 0: 
            print("Acertou!!")
            vitoria += 1
                
        else:
            print('VOCÊ PERDEU!!!')   
            break

    elif P_I == "I":
        if total % 2 == 0: 
            print('VOCÊ PERDEU!!!')
            print(f"Pois {total} é PAR!! ")
            vitoria += 1
                
        else:
            print("Acertou!!")
            print("Pois {total} é IMPAR")
            vitoria += 1
            break

