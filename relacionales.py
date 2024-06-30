def es_operador_relacional(lexema):
    
    if len(lexema) > 2:
        return False

    if lexema[0] in ['=', '!']:
        if len(lexema) == 2 and lexema[1] == '=':
            return True
        else:
            return False

    elif lexema[0] in ['<', '>']:
        if len(lexema) == 2 and lexema[1] == '=':
            return True

        return len(lexema) == 1

    else:
        return False
