valor1, operacao, valor2 = input("Texto: ").split()

if operacao == '+':
    print(float(valor1) + float(valor2))
if operacao == '-':
    print(float(valor1) - float(valor2))
if operacao == '*':
    print(float(valor1) * float(valor2))
if operacao == '/':
    print(float(valor1) / float(valor2))