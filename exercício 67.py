print("\033[1;36m-=-\033[m"*20)
Ndtb = cont = 0

while True:
    Ndtb = int(input("\033[1;35mQuer ver a tabuada de qual valor? \033[m" ))
    
    if Ndtb <= 0:
        print("\033[1;36m-=-\033[m"*20)
        break
    print("\033[1;36m-=-\033[m"*20)
    for c in range(1,11):
        r = Ndtb * c
        print(f"{Ndtb} * {c} = {r}")
    print("\033[1;36m-=-\033[m"*20)

    
print("\033[1;31mPROGRAMA DE TABUADA ENCERRADO.\033[m\033[1;32m Volte sempre!\033[m")
