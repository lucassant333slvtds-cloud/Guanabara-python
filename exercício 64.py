cont = 0
soma = 0
STOP = 0
while STOP != 999:
    STOP = int(input("digite 999 numero pra parar "))
    cont +=1
    soma += STOP
cont -= 1
soma -= 999
print(f"Paro!\nVocê digitou {cont} números ea soma entre eles foi {soma}.")
