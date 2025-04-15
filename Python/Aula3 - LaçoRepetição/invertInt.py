n = int(input("Digite um número inteiro sem dígito 0: "))

m = 0

if n == 0:
    print("O número não pode conter o dígito 0.")
else:
    while n > 0:
        m = m * 10 + (n % 10)  # 23 n = 23 -> m = 3 na volta m = 30 + n = 2 
        n = n - (n % 10)  # n = 20
        n = n // 10  # n = 2
    print(f"O número invertido é: {m}")