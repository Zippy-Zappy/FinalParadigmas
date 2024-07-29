def es_operador_asignacion(lexema):
    SIMBOLO_ASIGNACION = ["+=", '=', "*=", "/=", "%=", "-=", "**=", "//="]

    return lexema in SIMBOLO_ASIGNACION
