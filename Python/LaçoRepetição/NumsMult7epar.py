multiplos = 0
pares = 0
multPar = 0 

for i in range(5):
    valor = int(input("Informe um valor: "))

    if valor % 7 == 0:
        multiplos += 1
    
    if valor % 2 == 0:
        pares += 1

    if valor % 7 == 0 and valor % 2 == 0:
        multPar += 1

print(F"\nValores multiploes de 7: {multiplos} \nValores pares: {pares} \nValores múltiplos por 7 e pares: {multPar} ")