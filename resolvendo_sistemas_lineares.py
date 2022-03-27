#Um sistema de equações lineares do tipo: ax + by = c, e dx + ey = f, pode ser resolvido segundo mostrado a seguir: x = (ce - bf) / (ae - bd), y = (af - cd) / (ae - bd).
#Escreva um algoritmo que lê os coeficientes a, b, c, d, e e f e calcule e mostra os valores de x e y.

#Entradas e declaração de variáveis
a = float(input("Insira o coeficiente a: "))
b = float(input("Insira o coeficiente b: "))
c = float(input("Insira o coeficiente c: "))
d = float(input("Insira o coeficiente d: "))
e = float(input("Insira o coeficiente e: "))
f = float(input("Insira o coeficiente f: "))

#Processamento
x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

#Saída
print(f"X = {x}, y = {y}.")