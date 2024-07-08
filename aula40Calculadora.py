


while True:
    numero1 = input('Digite o primeiro numero: ')
    numero2 = input('Digite o segundo numero: ')
    operador = input('Digite a operação desejada: (+-/*)')

    numeros_validos = None
    numero1_float = 0
    numero2_float = 0

    ## Verificar os numeros
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Favor digite numeros validos!')
        continue

    ## Verificando o operador digitado

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if(operador == '/'):
        print(f'{numero1_float} / {numero2_float} = ', numero1_float / numero2_float)
    elif(operador == '*'):
        print(f'{numero1_float} * {numero2_float} = ', numero1_float * numero2_float)
    elif(operador == '-'):
        print(f'{numero1_float} - {numero2_float} = ', numero1_float - numero2_float)
    elif(operador == '+'):
        print(f'{numero1_float} + {numero2_float} = ', numero1_float + numero2_float)
    else:
        print('Não deveria chegar aqui')
        continue
    

    ## Sair do Programa    
    sair = input('Deseja sair do programa? [s]im: ').lower().startswith('s')

    if sair is True:
        break
    
print("Terminando operação...")