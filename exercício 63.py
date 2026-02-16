print("-=" * 20 )
print("Sequencia de Fibonacci ")
print("-=" * 20 )


T1 = 0
T2 = 1
c = 3

QTermos = int(input("Quantos termos vc quer mostrar?"))
print(f"{T1} → {T2}",end ='')
while c <= QTermos:
    T3 = T1 + T2
    print(f" → {T3}", end ='')
    T1 = T2
    T2 = T3
    c += 1
print(" cabo!")
