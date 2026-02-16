print("-="*10)
print(" |Gerador de PA |")
print("-="*10)
pterm = int(input("Qual o primeiro termo?"))
Rz = int(input("Qual a razão? "))
termo = pterm
cont = 1
total = 0
Mais = 10

while Mais != 0:
    total += Mais
    while cont <= total:
        print(f"{termo} → ", end=" ")
        termo += Rz
        cont += 1
    print("PAUSA!!")
    Mais = int(input("\nMais quantos termos?"))

print(f"Progressão finalizada com {total} termos!")
