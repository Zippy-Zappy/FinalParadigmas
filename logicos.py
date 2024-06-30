def es_operador_logico (lexema):
    
    if len(lexema)<= 3:

        if lexema[0] == "a":
            if lexema[1]== "n":
                if lexema[2]== "d":
                    return True
                else: 
                    return False
            else: 
                return False

        elif lexema[0] == "n":
            if lexema[1] == "o":
                if lexema[2] == "t":
                    return True
                else: 
                    return False
            else: 
                return False

        elif lexema[0] == "o":
            if lexema[1] == "r":
                return True
            else: 
                return False
        else: 
            return False
    else:
        return False
