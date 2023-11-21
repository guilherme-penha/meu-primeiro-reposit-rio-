import time

lista_de_compras = []

while True:
    menu = input('''Digite uma das opções para com a lista: 
  1° Adicionar um item a lista
  2° Remover um item da lista
  3° Alterar um item da lista
  4° Consultar a lista
  5° Limpar a lista
  6° Sair
  ''')

    if menu == '1':
        while True:
            time.sleep(1)
            item = input('Digite o item para adicionar a lista ou "X" para voltar ao menu \n').upper()
            if item == 'X':
                break
            else:
                time.sleep(1)
                lista_de_compras.append(item.title())
                print('O item foi adicionado!!')

    elif menu == '2':

        for i in range(len(lista_de_compras)):
            time.sleep(1)
            print(f'{i + 1}: {lista_de_compras[i]}')
        item = int(input('Digite o item para remover da lista: \n'))
        lista_de_compras.pop(item - 1)
        sleep(1)
        print('O item foi removido!!')
        sleep(2)
    elif menu == '3':
        for i in range(len(lista_de_compras)):
            time.sleep(1)
            print(f'{i + 1}: {lista_de_compras[i]}')
        item = int(input('Digite qual item você quer alterar na lista: \n'))
        produto = input('Digite o nome do produto: \n')
        lista_de_compras[item - 1] = produto
        sleep(1)
        print('O item foi alterado!!')
        sleep(2)
    elif menu == '4':
        for i in range(len(lista_de_compras)):
            time.sleep(1)
            print(f'{i + 1}: {lista_de_compras[i]}')
        escolha = input('Digite 1 para retornar ao menu anterior: ')
        if escolha == 1:
            continue
    elif menu == '5':
        lista_de_compras.clear()
        sleep(1)
        print('A lista foi zerada!!')
        sleep(2)
    else:
        break