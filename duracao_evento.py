#Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos

#Entrada de dados e declaração de variáveis
segundos_totais = int(input("Informe a duração do evento sem segundos: "))

#Processamento
horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais -(horas * 3600) - (minutos * 60)

#Saída
print(f"A duração do evento é de {horas} horas, {minutos} minutos e {segundos} segundos.")