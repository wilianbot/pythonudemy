
"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Luiz') # __iter__()
# print(texto)

texto = 'Luiz' # iterável
iterador = iter(texto) # iterator

while True:                         # Por baixo dos panos no for
    try:
        print(next(iterador))
    except StopIteration:
        break