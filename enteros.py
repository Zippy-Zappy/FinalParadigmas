def es_entero(lexema):
    Q0 = 0
    Q = [0, 1, 2, 3]
    F = [2]
    
    estado_actual = Q0
    indice = 0

    SIGMA = {
        "MENOS": 0,
        "DIGITO": 1,
        "OTRO": 2
    }

    DELTA = [
        [1, 2, 3], #transiciones de Q0
        [3, 2, 3], #transiciones de Q1
        [3, 2, 3], #transiciones de Q2
        [3, 3, 3] #transiciones del estado muerto
    ]

    def simbolo(caracter):
        if caracter >= '0' and caracter <= '9':
            return SIGMA["DIGITO"]
        if caracter == '-':
            return SIGMA["MENOS"]
        
        return SIGMA["OTRO"]

    while indice < len(lexema) and estado_actual != 3:
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        
        indice += 1
        
    return estado_actual in F
