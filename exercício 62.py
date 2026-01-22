print("-="*10)
print(" |Gerador de PA |")
print("-="*10)
pterm = int(input("Qual o primeiro termo?"))
Rz = int(input("Qual a razão"))
termo = pterm
cont = 1

while cont <= 10:
    print(f"{termo} → ", end=" ")
    termo += Rz
    cont += 1
    c = 0
    if cont == 10:
        Mais_termos = int(input("Qantos termos a mais ?"))
        while c <= Mais_termos:
            print(f"{_termo} → ", end=" ")
            
        
print("Cabo!")
