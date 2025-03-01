numero1 = int(input("Informe o primeiro número inteiro:"))

numero2 = int(input("Informe o segundo número:"))

if numero1 >= numero2:
    diferenca = numero1 - numero2    
else:
    diferenca = numero2 - numero1

print(f"A diferença entre o maior e menor número é de {diferenca}")

