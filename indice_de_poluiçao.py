indice = float(input("Informe o índice de poluição medido: "))

if (indice >= 0.05) and (indice <= 0.25):
    print("Os índices de poluição estão aceitáveis para todos os grupos.")
elif (indice > 0.25) and (indice < 0.4):
    print("As indústrias do grupo 1 devem suspender suas atividades.")
elif (indice > 0.4) and (indice < 0.5):
    print("As indústrias do grupo 1 e 2 devem suspender suas atividades.")
else:
    print("Todas as indústrias devem suspender suas atividades.")