import json

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
        
    return None


with open("names.json", "r") as file:
    dados = json.load(file)

list_with_128_names = dados["list_with_128_names"]
list_with_256_names = dados["list_with_256_names"]

print(pesquisa_binaria(list_with_128_names, "Carlos")) # -> 28
print(pesquisa_binaria(list_with_256_names, "Thaisa")) # -> None