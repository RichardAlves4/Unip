numero = int(input("Digite um número: "))
original = numero
reverso = 0

while numero > 0:
    digito = numero % 10 
    reverso = reverso * 10 + digito  
    numero //= 10  

if original == reverso:
    print(f"{original} é um palíndromo!")
else:
    print(f"{original} não é um palíndromo.")