import math as library

raio = int(input("Informe o raio do cilindro: "))

altura = int(input("Informe o tamanho da altura: "))

pi = library.pi

volumeCilindro = pi * (raio * raio) * altura

print(f"O volume do cilindro é de {volumeCilindro} m³")