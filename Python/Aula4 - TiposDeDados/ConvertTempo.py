anos = float(input("Digite a quantidade de anos: "))

meses = anos * 12
dias = anos * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print(f"\n{anos} ano(s) equivalem a:")
print(f"- {meses:.0f} meses")
print(f"- {dias:.0f} dias")
print(f"- {horas:.0f} horas")
print(f"- {minutos:.0f} minutos")
print(f"- {segundos:.0f} segundos")