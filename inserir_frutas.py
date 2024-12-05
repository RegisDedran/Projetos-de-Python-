""""
Adicionar itens em listas append(item): Adiciona um item ao final da lista. insert(posição, item): Insere um item em uma posição específica.

Editar itens em listas lista[posição] = "valor-atual"

Remover itens em listas: lista.remove(posição): Remove a primeira ocorrência do item especificado.

lista.pop(posição): Remove o item na posição especificada (ou o último item, se a posição não for passada).

lista.clear(): Remove todos os itens da lista, deixando-a vazia.

Métodos de Tuplas As tuplas são imutáveis, o que significa que não podem ser modificadas após serem criadas. Logo, você não pode adicionar, editar ou remover itens diretamente.

Se precisar modificar uma tupla, a solução é convertê-la em uma lista, fazer as alterações e depois convertê-la de volta para uma tupla

Clique duas vezes (ou pressione "Enter") para editar
"""
frutas = ["maçã","uva", "pera"]
frutas.insert(1,"limão") #escolhe a posição para inserir
frutas.append("uva") #adiciona um item no final da lista
for indice, item in enumerate(frutas):
  print(indice, item)
