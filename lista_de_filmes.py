filmes = {
    "Titanic": 2007,
    "Star Wars": 1977,
    "Strar Trek": 2009,
    "Matrix": 1999
}
filmes["Vingadores"] = 2012
print(filmes)


verficacao = input("Digite o nome de um filme: ")
if "verficacao" in filmes:
  print(f"{verficacao} está na lista")
else:
  print(f"O filme {verficacao} não está na lista")