#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias

#Declaração de variáveis e entrada de dados
idade_anos = int(input("Informe quantos anos completos de vida você tem: "))
idade_meses = int(input("Fora os anos de vida completos, informe quantos meses de vida você tem: "))
idade_dias = int(input("Fora os anos e meses de vida completos, informe quantos dias de vida você tem: "))

#Processamento
dias_vida = idade_anos * 365 + idade_meses * 30 + idade_dias

#Saída
print(f"A sua idade em dias é de: {dias_vida} dias")
