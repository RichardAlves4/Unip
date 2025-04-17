
def converte_para_romano(numero):
    romanos = [ 
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
    ]

    resultado = ""

    for valor, simbolo in romanos:
        while numero >= valor:
            resultado += simbolo
            numero -= valor

    return resultado

seculo = int(input("Digite o século (ex: 21): "))
romano = converte_para_romano(seculo)
print(f"Século {romano}")