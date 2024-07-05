nome = input('Qual o seu nome?')
print(f'O seu nome é {nome=}')

# nome= vai mostrar o nome da variavel antes

entrada = input('Voccê quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Voce entrou no sistema')
elif entrada == 'sair':
    print('Voce saiu do sistema')
else:
    print('Voce não digitou nem entrar nem sair') 