import time
print("Escolha de 1 á 5 para selecionar o jogo que quer jogar :")
nomes = {"1:":"GTA V" , "2:" : "Minecraft" , "3:" : "Call of duty", "4:" : "Farcry 4", "5:" : "Diablo 4"}
for x,y in nomes.items() :
    print(x , y)

jogo = (input("Digite aqui o jogo escolhido: "))
jogo = int(jogo)
if jogo == 1 :
    print("Iniciando GTA V, aguarde alguns segundos: ")
    t = 0
    for t in range (10) :
        t +=1
        time.sleep(1)
        print(t)
        if t == 10 :
            break
            print("Jogo pronto, Divirta-se ")

if jogo == 2 :
    print("Iniciando Minecraft, aguarde alguns segundos: ")
    t = 0
    for t in range (10) :
        t +=1
        time.sleep(1)
        print(t)
        if t == 10 :
            break
            print("Jogo pronto, Divirta-se ")
if jogo == 3 :
    print("Iniciando Call of duty, aguarde alguns segundos: ")
    t = 0
    for t in range (10) :
        t +=1
        time.sleep(1)
        print(t)
        if t == 10 :
            break
            print("Jogo pronto, Divirta-se ")
if jogo == 4 :
    print("Iniciando Farcry 4, aguarde alguns segundos: ")
    t = 0
    for t in range (10) :
        t +=1
        time.sleep(1)
        print(t)
        if t == 10 :
            break
print("Jogo pronto, Divirta-se ")
if jogo == 5 :
    print("Iniciando Diablo 4, aguarde alguns segundos: ")
    t = 0
    for t in range (10) :
        t +=1
        time.sleep(1)
        print(t)
        if t == 10 :
            print("esse é muito caro, joga outro rs ")
    for t in range(5):
        t += 1
        time.sleep(1)


    print("brinks, Jogo pronto, Divirta-se! ")
