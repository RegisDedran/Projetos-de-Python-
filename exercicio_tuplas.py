tupla = (1, 2, 3)
lista = list(tupla)  # Converte a tupla em lista
lista.append(4)  # Adiciona um item
tupla = tuple(lista)  # Converte a lista de volta em tupla
print(tupla)
