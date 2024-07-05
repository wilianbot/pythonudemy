# ------------------- NUMERO PAR E IMPAR ---------------------------------

# numero_str = input("Digite um numero inteiro: ")

# try:
#     numero_int = int(numero_str)
#     print("Numero inteiro")
#     if ((numero_int % 2) == 0):
#         print("Numero par")
#     else:
#         print("Numero impar")
# except:
#     print("Não é um numero inteiro!")



# -------------------------- HORARIO AO USUARIO ----------------------------------

# horario_str = input("Que horario é agora? ")

# try:
#     horario_int = int(horario_str)
#     if(horario_int > 0 and horario_int <= 11):
#         print("Bom dia")
#     elif(horario_int >= 12 and horario_int <= 17 ):
#         print("Boa tarde")
#     elif(horario_int >= 18 and horario_int <= 23):
#         print("Boa noite")
#     else:
#         print("Não conheço essa hora")
# except:
#     print("Digite um numero inteiro")

# ------------------------- NOME DO USUARIO ---------------------------------------

nome = input("Seu primeiro nome: ")

if (len(nome) > 1):
    print("Favor digite o nome correto")
elif (len(nome) <= 4):
    print("Seu nome é curto")
elif (len(nome) >= 5 and len(nome) <= 6):
    print('Seu nome é normal')
elif (len(nome) > 6):
    print('Seu nome é muito grande!')
