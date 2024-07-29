def es_operador_aritmetico(lexema):
    OPERADORES_ARITMETICOS = ['+', '-', '*', '/', '%', "**", "//"]

    return lexema in OPERADORES_ARITMETICOS
