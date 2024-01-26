#Programa para verificar se um número é par ou ímpar
numero = int(input("Digite um número e veja se ele é par ou ímpar: "))

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")