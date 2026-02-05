resp = "S"
cont = 0
soma = 0
media = 0
lista = []
while resp in 'Ss':
    n = int(input("Digite um número: "))
    lista.append(n)
    resp = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    cont += 1
    soma += n
media = soma / cont
print(f"Você digitou {cont} números e a media foi de {media}")
print(F"O maior valor foi {max(lista)} e o menor valor foi {min(lista)}")
