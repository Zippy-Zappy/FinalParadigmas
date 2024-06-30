def es_operador_asignacion(lexema):
    
    if len(lexema) > 3:
        return False

    if lexema[0] in ['+', '-', '%']:
        if len(lexema) == 2 and lexema[1] == '=':
            return True
        return False

    if lexema[0] in ['*', '/']:
        if len(lexema) == 2 and lexema[1] == '=':
            return True
        if len(lexema) == 3 and lexema[1] == lexema[0] and lexema[2] == '=':
            return True
        return False

    if lexema[0] == '=' and len(lexema) == 1:
        return True

    return False
