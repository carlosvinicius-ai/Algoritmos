def pesquisa_binaria(lista, item):
    baixo = 0
    # passamos a pesquisa desta forma por conta do index de pesquisa da lista
    alto = len(lista) - 1

    while baixo <= alto:
        # passamos o meio para diminuir o número de pesquisa passada
        meio = (baixo + alto) // 2
        chute = lista[meio]


        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
        
    # Caso item não seja encontrado o retorno será None    
    return None
    

# A lista deve ser ordenada para a pesquisa
minha_lista = [1, 3, 5, 7, 9]

# As listas começam no index 0 por isso o retorno é 1
print(pesquisa_binaria(minha_lista, 3)) # -> 1
print(pesquisa_binaria(minha_lista, -1)) # -> None