from random import randint
N_usuario = P_I = computador = cont = total = comparador = resultado = 0 
total = computador + N_usuario



print("P A R    O U    I M P A R ")
N_usuario = int(input("Dgigite um valor entre 1 e 10: "))
P_I = str(input("Par ou impar? (P/I) ")).strip()
computador = randint(0,10)
total = N_usuario + computador

while True:
    if total % 2 == 0: # PAR
        resultado = "Par"
        if resultado == P_I:
            print("Acertou!!")
            break
        else:
            print('errou!!!!')
            break

    else: #IMPAR
        resultado = "Impar"
        if resultado == P_I:
            print("VOCÊ VENCEU!!")
            break    
        else:
            print('VOCÊ PERDEU!!!\n TENTE NOVAMENTE!')
            break

print(f"Vc jogou {N_usuario} e o computaodr jogou {computador}. Total de {total}\n DEU {resultado}")