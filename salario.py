#salário gratificação

salario=float(input("Digite o salário: "))
tempo=int(input("Digite o tempo de serviço: "))

if salario>1500:
    if tempo<=3:
        salario=salario + 200
    else:
        salario=salario + 300
else:
    if tempo < 3:
        salario=salario + 230
    elif tempo < 6:
        salario = salario + 330
    else:
        salario=salario + 350
print("O novo salário é : ", salario)
