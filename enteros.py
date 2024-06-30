def es_entero(lexema):
    indice = 0
    if lexema[0] == '-':
        indice += 1

    if indice == len(lexema):
        return False

    while indice < len(lexema):
        if lexema[indice] < '0' or lexema[indice] > '9':
            return False
        indice += 1
    return True
