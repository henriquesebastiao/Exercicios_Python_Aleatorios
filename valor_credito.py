saldo_medio = float(input("Informe o seu saldo médio: "))

#Processamento
if saldo_medio <= 200:
    print(f"O seu saldo médio é de R$ {saldo_medio:.2f} e você não ganhou nenhum crédito.")
elif (saldo_medio >= 201) and (saldo_medio <= 400):
    credito = saldo_medio + (saldo_medio * 0.2)
    print(f"O seu saldo médio é de R$ {saldo_medio:.2f} e você ganhou R$ {credito:.2f} de crédito.")
elif (saldo_medio >= 401) and (saldo_medio <= 600):
    credito = saldo_medio + (saldo_medio * 0.3)
    print(f"O seu saldo médio é de R$ {saldo_medio:.2f} e você ganhou R$ {credito:.2f} de crédito.")
else:
    credito = saldo_medio + (saldo_medio * 0.4)
    print(f"O seu saldo médio é de R$ {saldo_medio:.2f} e você ganhou R$ {credito:.2f} de crédito.")