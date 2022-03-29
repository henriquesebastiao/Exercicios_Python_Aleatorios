#Entrada de dados:
identificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))
nota3 = float(input("Informe a terceira nota do aluno: "))
me = float(input("Informe a média dos exercícios: "))

#Calculando a média de aproveitamento:
ma = (nota1 + nota2 * 2 + nota3 * 3 + me) / 7

#Informando conceito do aluno de acordo com a média de aproveitamento:
if ma >= 9.0:
    print(f"O número de identificação do aluno é: {identificacao}")
    print(f"As notas das três provas do aluno são, respectivamente: {nota1}; {nota2} e {nota3}")
    print(f"A média dos exercícios do aluno é de: {me}")
    print(f"A média de aproveitamento do aluno é de: {ma:.2f}")
    print(f"O conceito do aluno é: A")
    print("APROVADO")
elif (ma >= 7.5) and (ma < 9.0):
    print(f"O número de identificação do aluno é: {identificacao}")
    print(f"As notas das três provas do aluno são, respectivamente: {nota1}; {nota2} e {nota3}")
    print(f"A média dos exercícios do aluno é de: {me}")
    print(f"A média de aproveitamento do aluno é de: {ma:.2f}")
    print(f"O conceito do aluno é: B")
    print("APROVADO")
elif (ma >= 6.0) and (ma < 7.5):
    print(f"O número de identificação do aluno é: {identificacao}")
    print(f"As notas das três provas do aluno são, respectivamente: {nota1}; {nota2} e {nota3}")
    print(f"A média dos exercícios do aluno é de: {me}")
    print(f"A média de aproveitamento do aluno é de: {ma:.2f}")
    print(f"O conceito do aluno é: C")
    print("APROVADO")
elif (ma >= 4.0) and (ma < 6.0):
    print(f"O número de identificação do aluno é: {identificacao}")
    print(f"As notas das três provas do aluno são, respectivamente: {nota1}; {nota2} e {nota3}")
    print(f"A média dos exercícios do aluno é de: {me}")
    print(f"A média de aproveitamento do aluno é de: {ma:.2f}")
    print(f"O conceito do aluno é: D")
    print("REPROVADO")
else:
    print(f"O número de identificação do aluno é: {identificacao}")
    print(f"As notas das três provas do aluno são, respectivamente: {nota1}; {nota2} e {nota3}")
    print(f"A média dos exercícios do aluno é de: {me}")
    print(f"A média de aproveitamento do aluno é de: {ma:.2f}")
    print(f"O conceito do aluno é: E")
    print("REPROVADO")