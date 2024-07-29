def es_operador_logico (lexema):
    Q = [0, 1, 2]
    Q0 = 0
    F = 1

    SIGMA = {
        "and": 0,
        "or": 1,
        "not": 2,
        "o": 3,  # Otros
    }

    DELTA = [
        [1, 1, 1, 2],  # Estado 0
        [2, 2, 2, 2],  # Estado 1
        [2, 2, 2, 2],  # Estado 2 (Muerto)
    ]

    def obtener_lexema_index(lexema):
        """Devuelve el indice del lexema que se encuentre en SIGMA."""

        if lexema in SIGMA:
            return SIGMA[lexema]

        return SIGMA["o"]


    estado_actual = Q0

    lexema_index = obtener_lexema_index(lexema)
    estado_actual = DELTA[estado_actual][lexema_index]

    if estado_actual == 2:
        return False

    return estado_actual == F
