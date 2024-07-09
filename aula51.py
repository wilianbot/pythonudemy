#  Introdução ao desempacotamento + tuples (tuplas)

# nomes = ['Maria', 'Helena', 'Luiz', 'Gui']
# nome1, nome2, nome3, nome4 = nomes
# print(nome4)

# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# print(nome3)

nome1, nome2, *resto = ['Maria', 'Helena', 'Luiz', 'Gui']
print(nome1, nome2, resto)