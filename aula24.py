# Operadores in e not in
# String são  iteraveis - Pode nevagar item por item utilizando os indices
# 0 1 2 3 4 5
# O t á v i o
#-6-5-4-3-2-1

# ---------------------------------------------------------------------------------

# nome = 'Otávio'
# print(nome[2]) # Vai imprimir o indice 2 que está no nome 
 
# print('á' in nome) # Se estiver 'á' entre o nome vai retornar true 

# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

# nome = input('Digite seu nome: ')
# enconrar =input('Digite o que deseja encontrar: ')

# ---------------------------------------------------------------------------------

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}' )
else:
    print(f'{encontrar} não está em {nome}')