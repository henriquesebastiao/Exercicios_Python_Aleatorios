#Um usuário deseja um algoritmo onde possa escolher que tipo de média deseja calcular a partir de 3 notas. Faça um algoritmo que leia as notas, a opção escolhida pelo usuário e calcule a média
#1 -aritmética
#2 -ponderada (3,3,4)
#3 -ponderada (3,3,4)

print("Tipos de médias disponíveis:")
print("1 - Aritmética")
print("2 - Ponderada (3, 3, 4)")
print("3 - Harmônica")
opcao = int(input("Informe o tipo desejado: "))

if (opcao < 1) or (opcao > 3):
    print("O tipo informado é inválido. Tente novamente.")
else:
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    nota3 = float(input("Insira a terceira nota: "))

    if opcao == 1:
        media = (nota1 + nota2 + nota3) / 3
        print(f"A média do aluno é {media:.2f}")
    elif opcao == 2:
        media = ((nota1 * 3) + (nota2 * 3) + (nota3 * 4)) / 10
        print(f"A média do aluno é {media:.2f}")
    else:
        media = 3 / ((nota1 ** -1) + (nota2 ** -1) + (nota3 ** -1))
        print(f"A média do aluno é {media:.2f}")