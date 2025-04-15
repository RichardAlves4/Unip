#Dada a quantidade de alunos de uma turma, calcular a média semestral de cada aluno
#da turma e mostrar uma mensagem para os alunos aprovados.

aluno = int(input("Informe quantos alunos há na turma: "))

saida = "\nResultados finais:\n"

for turma in range(aluno):

    nota1 = float(input("Informe a primeira nota: "))
    
    nota2 = float(input("Informe a segunda nota: "))
    
    media = (nota1 + nota2)/2

    if media < 5:
        resultado = "Aluno reprovado "
    
    elif media < 7:
        resultado = "Aluno de recuperação "
    
    else:
        resultado =  "Aluno aprovado"

    saida += f"Aluno {turma+1}: Média {media} - {resultado}\n"

print(saida) 