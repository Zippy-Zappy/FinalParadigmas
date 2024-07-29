def es_simbolo_de_puntuacion(lexema):
    SIMBOLO_PUNTUACION = [',', '.', ':', '"', "'", '{', '}', '(', ')', '[', ']']

    return lexema in SIMBOLO_PUNTUACION
