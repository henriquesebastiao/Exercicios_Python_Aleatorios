#Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:
#infantil A = 5 - 7 anos
#infantil B = 8-10 anos
#juvenil A = 11-13 anos
#juvenil B = 14-17 anos
#adulto = maiores de 18 anos

#Entrada de dados e declaração de variáveis:
idade = int(input("Informe a idade do nadador: "))

#Processamento:
if (idade >= 5) and (idade <= 7):
    print("O nadador está na categoria infantil A.")
elif (idade >= 8) and (idade <= 10):
    print("O nadador está na categoria infaltil B.")
elif (idade >= 11) and (idade <= 13):
    print("O nadador está na categoria juvenil A.")
elif (idade >= 14) and (idade <= 17):
    print("O nadador está na categoria juvenil B.")
else:
    print("O nadador está na categoria adulto.")