def es_identificador(lexema: str) -> bool:
    ESTADO_INICIAL = 0
    F = [2]
    Q = range(3)

    logicos = ["and", "not", "or"]

    SIGMA = {
        "LETRA": 0,  
        "GUION_BAJO": 1,
        "DIGITO": 2,
        "OTRO": 3
    }

    DELTA = [
        [2, 2, 1, 1], 
        [1, 1, 1, 1],  
        [2, 2, 2, 1], 
    ]

    # Evaluar Caracter
    def simbolo(caracter: str) -> int:
        if ('a' <= caracter <= 'z') or ('A' <= caracter <= 'Z'):
            return SIGMA["LETRA"]
        elif caracter == "_":
            return SIGMA["GUION_BAJO"]
        elif "0" <= caracter <= "9": 
            return SIGMA["DIGITO"]
        else:
            return SIGMA["OTRO"]

    estado_actual = ESTADO_INICIAL
    indice = 0

    if lexema in logicos:
        estado_actual = 1

    while indice < len(lexema) and estado_actual != 1:
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        indice += 1

    return estado_actual in F