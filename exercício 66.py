total = n = cont = 0 
while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    cont += 1
    total += n
print(f"A soma dos {cont - 1} valores foi {total - 999}!")