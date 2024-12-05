
#Solicitamos a nota do usuário e a convertendo para um número decimal usando float().
#Nota >= 9 ( A )
#Nota >= 7 ( B )
#Nota >= 5 ( C )

nota = float(input("Digite sua Nota: "))
if nota >= 9:
  if nota >= 11:
    print('Nota inválida:')
  else:
    print('Você tirou nota : A')
elif nota >= 7:
  print('Você tirou nota : B')
elif nota >=5:
  print('Você tirou nota : C')
else:
  print('Você tirou nota : D')