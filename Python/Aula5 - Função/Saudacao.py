def saudacao(recebe_nome):
    
    return f"Bem-vindo viajante {recebe_nome}"

nome = str(input("Informe o seu nome: "))
mensagem = saudacao(nome)

print(mensagem)