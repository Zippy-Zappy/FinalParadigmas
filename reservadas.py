def es_palabra_reservada(lexema):
    RESERVADAS = ["def", "if", "import", "for", "while", "else", "elif", "return", "with", "as", "range", "in"]

    return lexema in RESERVADAS