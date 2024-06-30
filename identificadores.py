def es_letra(caracter):
    return ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z')

def es_digito(caracter):
    return '0' <= caracter <= '9'

def es_identificador(lexema, indice=0):
    operadores_logicos = ["and", "or", "not"]

    if len(lexema) == 0:
        return False
    
    if lexema in operadores_logicos:
        return False
    
    if indice == 0:
        if not (es_letra(lexema[indice]) or lexema[indice] == '_'):
            return False
    else:
        if not (es_letra(lexema[indice]) or es_digito(lexema[indice]) or lexema[indice] == '_'):
            return False

    if indice == len(lexema) - 1:
        return True

    return es_identificador(lexema, indice + 1)