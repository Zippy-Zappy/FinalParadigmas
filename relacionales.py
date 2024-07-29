def es_operador_relacional(lexema):
    """Recorre la cadena de entrada y utiliza la tabla de transición DELTA 
    para determinar si la cadena es un operador relacional válido."""
    Q0 = 0 # Estado inicial
    Q = [0, 1, 2, 3, 4]
    F = [2, 3] # Estados finales


    SIGMA = {
        "=": 0,
        "<": 1,
        ">": 2,
        "!": 3,
        "o": 4,
    }

    DELTA = [
        [1, 2, 2, 1, 4],  # Estado 0
        [3, 4, 4, 4, 4],  # Estado 1
        [3, 4, 4, 4, 4],  # Estado 2
        [4, 4, 4, 4, 4], # Estado 3
        [4, 4, 4, 4, 4]  # Estado 4 (Estado muerto)
    ]


    def obtener_simbolo_index(simbolo):
        """Devuelve el índice del símbolo según el diccionario SIGMA."""

        if simbolo in SIGMA:
            return SIGMA[simbolo]

        return SIGMA["o"]



    estado_actual = Q0  # Estado inicial

    for simbolo in lexema:
        simbolo_index = obtener_simbolo_index(simbolo)
        estado_actual = DELTA[estado_actual][simbolo_index]

        if estado_actual == 4:  # Estado muerto
            return False

    return estado_actual in F  # Verifica si el estado final es válido
