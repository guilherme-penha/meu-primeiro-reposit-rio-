cpf = input('Digite o seu cpf: ')

# tratamento do cpf

cpf = cpf.replace('.','')
cpf = cpf.replace('-','')

if len(cpf) != 11 or cpf.isdigit() == False:
  print('Digite um cpf válido!!!')


cpf_digito_1 = int(cpf[-2:-1])
cpf_digito_2 = int(cpf[-1])
cpf_1 = cpf[:9]
cpf_2 = cpf[:10]

#verficação do cpf
soma_1 = 0
numero_1 = 10
soma_2 = 0
numero_2 = 11

for digito in cpf_1:
  soma_1 += int(digito) * numero_1
  numero_1 -= 1

for digito in cpf_2:
  soma_2 += int(digito) * numero_2
  numero_2 -= 1

soma_1 = soma_1 *10
soma_1 = soma_1%11
soma_2 = soma_2 *10
soma_2 = soma_2%11

if soma_1 > 9:
  soma_1 == 0
else:
  soma_1 = soma_1

if soma_2 > 9:
  soma_2 == 0
else:
  soma_2 = soma_2

if soma_1 == cpf_digito_1 and soma_2 == cpf_digito_2:
  print('Cpf Válido!!!')
else:
  print('CANCELADO')