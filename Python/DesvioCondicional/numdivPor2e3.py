#O operador % (módulo) retorna o resto da divisão entre dois números.

numero = int(input("Informe um númeroe descubra se ele é divisível por 2 e 3: "))

if numero % 2 == 0 and numero % 3 == 0:
    print(f"O {numero} é divisível por 2 e 3")
else:
    print(f"O {numero} não é divisível por 2 e 3")