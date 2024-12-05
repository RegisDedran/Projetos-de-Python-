#Verificar se o número é positivo ou negativo Escreva um 
#programa que peça ao usuário para digitar um número e use a estrutura if para verificar se o 
#número é positivo ou negativo. Exiba a mensagem correspondente. 

numero = float(input("Digite um número"))
if numero == 0:
  print(f'{numero} e igual a zero')
elif numero > 0:
    print(f'{numero}positivo')
else:
  print(f'{numero} negativo')