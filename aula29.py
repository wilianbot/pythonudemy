# numero_str = input("Vou dobrar o número que vc digitas: ")

# numero_float = float(numero_str) # Transformando uma string em float
# print(f"O dobro de {numero_float} é {numero_float * 2}")

numero_str = input (
    'Vou dobrar o número que vc digitar: '
)

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
# else:
#     print('Isso nã o é um número')


try: 
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')
