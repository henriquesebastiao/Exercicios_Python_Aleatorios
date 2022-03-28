#Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo com o cargo, conforme a tabela abaixo. Faça um algoritmo que leia o salário e o cargo de um funcionário e calcule o novo salário. Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber 40% de aumento. Mostre o salário antigo, o novo salário e a diferença.

#Entrada de dados e declaração de variáveis
salario = float(input("Informe o salário do funcionário: "))
codigo = int(input("Informe o código do funcionário: "))

#Processamento e saída de dados
if (codigo != 101) and (codigo != 102) and (codigo != 103):
    aumento = salario * 0.40
    novo_salario = salario + aumento
    print(f"O salário antigo do funcionário era de R$ {salario}, o novo salário é de R$ {novo_salario} e a diferença é de R$ {aumento}.")
elif codigo == 101:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"O salário antigo do funcionário era de R$ {salario}, o novo salário é de R$ {novo_salario} e a diferença é de R$ {aumento}.")
elif codigo == 102:
    aumento = salario * 0.20
    novo_salario = salario + aumento
    print(f"O salário antigo do funcionário era de R$ {salario}, o novo salário é de R$ {novo_salario} e a diferença é de R$ {aumento}.")
else:
    aumento = salario * 0.30
    novo_salario = salario + aumento
    print(f"O salário antigo do funcionário era de R$ {salario}, o novo salário é de R$ {novo_salario} e a diferença é de R$ {aumento}.")