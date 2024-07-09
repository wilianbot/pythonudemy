# lista = [123, True, 'Luiz Otávio', 1.2, []]
# lista[0] = 'maria'
# print(lista)
# print(lista[2], type(lista[2]))


# lista = [10, 20, 30, 40, 50, 60]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

# lista.append(50)
# lista.pop()
# lista.pop()
# lista.append(60)
# lista.append('TESTE')
# ultimo_valor = lista.pop()
# print(lista, 'Removido,', ultimo_valor)


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

print(lista_c)

lista_d = lista_a.extend(lista_b)

print(lista_a)