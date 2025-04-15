habitante = int(input("Informe o total de habitantes: "))

maiorIdade = 0

fem18_35 = 0

saida = "\nLista de Habitantes\n"

for i in range(habitante):
    
    print("Digite -1 em idade para encerrar o programa.")
    
    idade = int(input("Informe a idade do habitante: "))

    if idade == -1:
        break

    if idade > maiorIdade:
        maiorIdade = idade

    sexo = input("Digite M para masculino e F para feminino: ")

    if sexo == "M" or sexo == "m" or sexo == "F" or sexo == "f":

        saida += f"\n{i+1} Idade: {idade} | Gênero: {sexo}" 
 
        if sexo == "F" and idade >= 18 and idade <=35  or sexo == "f" and idade >= 18 and idade <= 35:
            fem18_35 += 1

percentfem = (fem18_35 * 100) / habitante

print(saida)

print(f"\nMaior Idade registrada: {maiorIdade}")

print(f"Total de Mulheres com idade entre 18 e 35: {fem18_35}")

print(f"Percentual de mulheres com idade entre 18 e 35: {percentfem}%")
    
    
