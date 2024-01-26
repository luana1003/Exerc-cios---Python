#Programa para verificar a validade de senhas e nomes
nome = input("Digite um nome: ")
nome_correto = "Luana"
senha = input("Digite uma senha: ")
senha_correta = input("python3.12")

def verificar_senha_e_usuario():
    if(nome == nome_correto and senha == senha_correta):
        print("Você acertou o nome e a senha!")
    else:
        print("Você errou o nome e a senha!")

verificar_senha_e_usuario()