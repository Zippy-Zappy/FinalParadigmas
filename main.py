import analizador
import re

DELIMITADORES = r'(".*?"|\d+(\.\d+)?([eE][-+]?\d+)?|[a-zA-Z_]\w*|==|!=|<=|>=|[\+\-\*/=(),;:.{}[\]]+)'

with open("token.txt", "r") as archivo:
    texto = archivo.read()

tokens = [token[0] for token in re.findall(DELIMITADORES, texto)]
tokens = [token.strip() for token in tokens if token.strip()]

with open("output.txt", 'w') as archivo_nuevo:
    for token in tokens:
        output = analizador.analizar_lexicamente(token)
        print(output)
        archivo_nuevo.write(output + "\n")
