#Programa para categorizar a idade de um usuário
idade_usuario = int(input("Digite sua idade:"))

def verificar_idade_usuario():
    if(idade_usuario >= 0 and idade_usuario <=12):
        print(f"Criança: 0 a 12 anos pois sua idade é {idade_usuario} anos")

    elif(idade_usuario >= 13 and idade_usuario <=18):
        print(f"Adolescente: 13 a 18 anos pois sua idade é {idade_usuario} anos")

    elif(idade_usuario > 18):
        print(f"Adulto: acima de 18 anos, pois sua idade é {idade_usuario} anos")

verificar_idade_usuario()