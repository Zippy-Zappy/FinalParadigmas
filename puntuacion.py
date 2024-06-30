def es_simbolo_de_puntuacion(lexema):
    
    if len(lexema) == 1:
        if lexema in [',', '.', ':', '"', "'"]:
            return True
        else: 
            return False
        
    elif len(lexema) == 2:
        if lexema[0] == '"':
            if lexema[1] == '"':
                return True
            else: 
                return False
            
        elif lexema[0] == "'":
            if lexema[1] == "'":
                return True
            else: 
                return False
        
        elif lexema[0] == "(":
            if lexema[1] == ")":
                return True
            else: 
                return False
            
        elif lexema[0] == "[":
            if lexema[1] == "]":
                return True
            else: 
                return False
            
        elif lexema[0] == "{":
            if lexema[1] == "}":
                return True
            else: 
                return False
            
        else:
            return False

    else:
        return False
