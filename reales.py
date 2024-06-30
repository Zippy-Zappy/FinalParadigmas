def es_real(lexema):
    """
    Verifica si una cadena es un número entero o decimal válido según los criterios especificados.
    Un número válido puede ser:
    - Un número entero (positivo o negativo).
    - Un número decimal (positivo o negativo) con un punto decimal ('.') en cualquier posición.
    """
    if not lexema:  # Si la cadena está vacía, no es un número válido
        return False

    # Verificar si es un número negativo
    if lexema[0] == '-':
        if len(lexema) == 1:  # Un solo '-' no es un número válido
            return False
        start_index = 1
    else:
        start_index = 0

    # Variables de control
    tiene_punto = False
    tiene_digitos = False

    # Verificar cada carácter a partir del índice de inicio
    for i in range(start_index, len(lexema)):
        if lexema[i] == '.':
            if tiene_punto:  # Si ya hay un punto, no puede haber otro
                return False
            tiene_punto = True
        elif '0' <= lexema[i] <= '9':
            tiene_digitos = True
        else:
            return False

    # Para ser válido debe tener al menos un dígito y un punto
    return tiene_digitos and tiene_punto  # Devuelve True si hemos encontrado al menos un dígito y un punto, de lo contrario False
