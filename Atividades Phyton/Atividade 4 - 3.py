while True:
    cpf = input('Digite seu cpf para validação: \n')
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if (cpf.isdecimal() == False) or (len(cpf) != 11):
        print('Cpf inválido!!! Digite outro. ')
    cpf_digito = cpf[-2:-1]
    cpf = cpf[:9]

    soma = 0
    valor = 10
    for numero in cpf:
        soma += int(numero) * valor
        valor -= 1

    soma = soma * 10
    soma = soma % 11

    if soma > 9:
        soma = 0
    else:
        soma = soma

    if soma == int(cpf_digito):
        print('Cpf Valido!!!!')
    else:
        print('CPF CANCELADO!!!!!!')