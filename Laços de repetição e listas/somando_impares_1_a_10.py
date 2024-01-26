#Programa para somar todos os números ímpares de 1 a 10
def somar_impares_de_1_a_10():
    soma_impares = 0
    for numero in range (1,11):
        if numero % 2 != 0:
            soma_impares += numero
    print(soma_impares)

somar_impares_de_1_a_10()
