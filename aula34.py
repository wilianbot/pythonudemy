condicao = True
while condicao:
    inOut = input('[C]ontinuar ou [S]air: ')
    if inOut == 'C' or inOut == 'c':
        nome = input('Qual é o seu nome:')
        print(f'Seu nome é {nome}')
    elif inOut == 'S' or inOut == 's':
        print('Saindo do programa...')
        condicao = False


