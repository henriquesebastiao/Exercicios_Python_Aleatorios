#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor

#Entradas e declarações de variáveis
custo_fabrica = float(input("Informe o custo de fábrica do carro: "))

#Processamento
custo_consummidor = custo_fabrica + (custo_fabrica * 0.28) + (custo_fabrica * 0.45)

#Saída
print(f"O custo do carro para o consumidor é de R${custo_consummidor:.2f}")