#Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente

#Declaração de variáveis e entrada de dados
nota1 = float(input("Informa a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

#Processamento
media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / (2 + 3 + 5)

#Saída
print(f"A média do aluno é {media}")