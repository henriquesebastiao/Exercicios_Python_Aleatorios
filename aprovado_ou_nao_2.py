#Entradas
codigo = input("Informe o código do aluno: ")
nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))
nota3 = float(input("Informe a terceira nota do aluno: "))

#Achando a maior nota:
maior = nota1
if nota2 > maior:
    maior = nota2
if nota3 > maior:
    maior = nota3

if (maior > nota1) and (maior > nota2):
    media = ((maior * 4) + (nota1 * 3) + (nota2 * 3)) / 10
    print(f"As notas do aluno são, respectivamente: {nota1:.2f}, {nota2:.2f}, {nota3:.2f}. O código do aluno é {codigo} e média do aluno é {media:.2f}.")
elif (maior > nota2) and (maior > nota3):
    media = ((maior * 4) + (nota2 * 3) + (nota3 * 3)) / 10
    print(f"As notas do aluno são, respectivamente: {nota1:.2f}, {nota2:.2f}, {nota3:.2f}. O código do aluno é {codigo} e média do aluno é {media:.2f}.")
else:
    media = ((maior * 4) + (nota1 * 3) + (nota3 * 3)) / 10
    print(f"As notas do aluno são, respectivamente: {nota1:.2f}, {nota2:.2f}, {nota3:.2f}. O código do aluno é {codigo} e média do aluno é {media:.2f}.")

if media >= 5:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")