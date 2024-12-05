""""
Métodos de Dicionários Adicionar ou Editar itens em dicionários No dicionário, adicionar ou editar itens 
usa a mesma sintaxe: atribuir um valor a uma chave. Se a chave já existe, o valor é atualizado; se não existe, 
o par chave-valor é adicionado.

método .get() em Python é usado com dicionários para acessar o valor de uma chave, mas de forma mais segura. Ele funciona assim:

Se a chave existir no dicionário, ele retorna o valor correspondente. Se a chave não existir, ao 
invés de causar um erro, o método retorna um valor padrão que você pode definir. Se não definir um valor padrão, ele retorna None.
"""
dicionario = {"nome": "João", "idade": 25}
dicionario["cidade"] = "São Paulo"  # Adiciona um novo par chave-valor
dicionario["idade"] = 30  # Atualiza o valor da chave "idade"
dicionario.pop("idade")  # Remove o par cuja chave é "idade"
del dicionario["cidade"]  # Remove o par cuja chave é "cidade"
print(dicionario)

dicionario.clear()  # Limpa o dicionário

material_escolar = ["","","","Caderno"]
material_escolar[0] = input("Digite o nome do material: ")
material_escolar[1] = input("Digite o nome do material: ")
material_escolar[2] = input("Digite o nome do material: ")
print(material_escolar)

dicionario = {
    "fruta1": "maçã",
    "fruta2": "banana",
    "fruta3": "laranja"
}
for chave, palavra in dicionario.items():
    print(f"/n Letras da {chave}:")
    for letra in palavra:
      print(letra)
