#Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
#Exemplo: Para n = 4, a saída deverá ser 1, 3, 5, 7

num = int(input("Informe um número que seja inteiro e positivo: "))

contador = 0

inpar = 1 

while contador < num:
    print(f"{inpar}")
    inpar += 2

    contador += 1

    
