
def nome_ju(texto) :   # (def == função)  (nome_ju == Nome da função)  ((texto) = parametro)
    texto = texto.split() # ((texto=) = Variavel) (texto.split()) = responsavel por dividir a string OBS: )
    lista = [] # Criei uma lista para armazenar os dados da varialvel lista
    for palavra in texto: #for - para  palavra = alguma coisa  in = dentro  texto: = de texto
        if len(palavra) == 2:
            palavra = palavra [::-1]
            lista.append(palavra)
        else :
            palavra = palavra[-3:] + palavra [0:-3]
            lista.append(palavra)
    return " " .join(lista)

print(nome_ju("macaco azul"))