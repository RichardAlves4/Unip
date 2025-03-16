n = int(input("Escreva um número inteiro que não seja 0: "))

m = 0 

while n > 0:

    m = (n % 10) #m = ultimo digito de n       
    n // 10

print(f"O número invertido é: {m}")