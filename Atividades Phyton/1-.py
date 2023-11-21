import random



numero_1 = 0
numero_2 = 0
numero_3 = 0

while True:
    numero_aleatorio = random.randint( 1,3 )
    numeroA = numero_aleatorio
    if numero_1 == 10000 or numero_2 == 10000 or numero_3 == 10000 :
        break
    elif numeroA == 1 :
        numero_1 +=1
    elif numeroA == 2:
        numero_2 +=1
    elif numeroA == 3:
        numero_3 +=1

print("1= " + str(numero_1))
print("2= " + str(numero_2))
print("3= " + str(numero_2))
