num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
  print(f'O Resultado será : {num1 + num2}')
elif operacao == '-':
  print(f'O Resultado será: {num1 - num2}')
elif operacao == '*':
  print(f'O Resultado será: {num1 * num2}')
elif operacao == '/':
  if num2 != 0:
    print(f'O Resultado será: {num1 / num2}')
  else:
    print(f'Erro de divisão por zero')
else:
  print("Operação inválida")

#outra forma

def calculadora(valor1,valor2,operacao):

  if operacao == 'soma':
    print(valor1 + valor2)
  elif operacao == 'subtracao':
    print(valor1 - valor2)
  elif operacao == 'multiplicacao':
    print(valor1 * valor2)
  elif operacao == 'divisao':
    print(valor1 / valor2)
  else:
    print("Operacao invalida")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operacao1: ")

calculadora(valor1,valor2,operacao)