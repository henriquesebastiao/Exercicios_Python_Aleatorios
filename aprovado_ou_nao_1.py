#Calcule a média aritmética das 3 notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado", caso a média seja igual ou superior a 6, ou a mensagem "reprovado", caso contrário

#Entrada de dados e declaração de variáveis
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

#Processo
media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")