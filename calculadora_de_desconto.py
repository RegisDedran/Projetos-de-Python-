#Compras acima de R$1000: 15% de desconto.
#Compras entre R 500eR 1000: 10% de desconto.
#Compras abaixo de R$500: 5% de desconto.
#Formula: valor_final = valor - (valor * desconto)

valor = float(input("Digite o valor da compra: "))
if valor > 1000:
  desconto = 0.15
elif valor >= 500:
  desconto = 0.10
else:
  desconto = 0.05
valor_final = valor - (valor * desconto)
print(f'O valor final da compra é: R${valor_final:.2f}')
