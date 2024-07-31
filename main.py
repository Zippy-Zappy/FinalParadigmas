import analizador
import re

DELIMITADORES = r'''
(?P<STRING>"[^"]*"|'[^']*') |
(?P<NUMBER>-?\d*\.\d+|-?\d+\.\d*|-?\d+(?:[eE][-+]?\d+)?|\d+(?:[eE][-+]?\d+)?) |
(?P<IDENTIFIER>[a-zA-Z_]\w*) |
(?P<RELATIONAL>==|!=|<=|>=|<|>) |
(?P<ARITHMETIC>\+|-|\*|\/) |
(?P<ASSIGNMENT>=) |
(?P<PUNCTUATION>\(|\)|,|;|:|\.|{|}|\[|\]) |
(?P<RESERVED>\bimport\b|\bdef\b|\bif\b|\belse\b|\belif\b|\breturn\b)
'''

with open("token.txt", "r") as archivo:
    texto = archivo.read()


tokens = [match.group() for match in re.finditer(DELIMITADORES, texto, re.VERBOSE)]
tokens = [token.strip() for token in tokens if token.strip()]

with open("output.txt", 'w') as archivo_nuevo:
    for token in tokens:
        output = analizador.analizar_lexicamente(token)
        archivo_nuevo.write(output + "\n")
