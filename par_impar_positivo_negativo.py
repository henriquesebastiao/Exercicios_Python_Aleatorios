#Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo

#Declaração de variáveis
numero = int(input("Informe um número: "))

#Processamento
par_impar = numero % 2

if par_impar == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

if numero >= 0:
    print("O numero é positivo.")
else:
    print("O número é negativo.")