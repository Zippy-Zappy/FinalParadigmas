def es_string(lexema: str) -> bool:
    if lexema[0] == '"' and lexema[-1] == '"':
        return True
    if lexema[0] == "'" and lexema[-1] == "'":
        return True
    return False