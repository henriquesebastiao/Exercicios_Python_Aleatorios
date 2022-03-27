#O cardápio de uma lancheria é o seguinte:
#Cachorro quente (código: 100)(valor: 1,20)
#Bauru simples (código: 101)(valor: 1,30)
#Bauru com ovo (código: 102)(valor: 1,50)
#Hambúrguer (código: 103)(valor: 1,20)
#Cheeseburguer (código: 104)(valor: 1,30)
#Refrigerante (código: 105)(valor; 1,00)
#Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um item.

codigo = int(input("Informe o código do item desejado: "))

if (codigo >= 100) and (codigo <= 105):
    
    quantidade = int(input("Informe a quantidade desejada: "))
    
    if codigo == 100:
        valor = quantidade * 1.20
        print(f"O valor do seu pedido é de R$ {valor:.2f}")
    elif codigo == 101:
        valor = quantidade * 1.30
        print(f"O valor do seu pedido é de R$ {valor:.2f}")
    elif codigo == 102:
        valor = quantidade * 1.50
        print(f"O valor do seu pedido é de R$ {valor:.2f}")
    elif codigo == 103:
        valor = quantidade * 1.20
        print(f"O valor do seu pedido é de R$ {valor:.2f}")
    elif codigo == 104:
        valor = quantidade * 1.30
        print(f"O valor do seu pedido é de R$ {valor:.2f}")
    else:
        valor = quantidade * 1.00
        print(f"O valor do seu pedido é de R$ {valor:.2f}")
else:
    print("O código informado é inválido. Tente novamente.")