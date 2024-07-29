import aritmeticos
import asignacion
import enteros
import es_string
import identificadores
import logicos
import puntuacion
import relacionales
import reales
import reservadas

def analizar_lexicamente(lexema):

    if len(lexema) < 1:
        return("Error. El lexema ingresado no debe estar vacío.")
    else:
        devolucion = f"El lexema '{lexema}' es un"
        if reales.es_real(lexema):
            devolucion += " número real."
        elif enteros.es_entero(lexema):
            devolucion += " número entero."
        elif reservadas.es_palabra_reservada(lexema):
            devolucion += "a palabra reservada."
        elif identificadores.es_identificador(lexema):
            devolucion += " identificador."
        elif es_string.es_string(lexema):
            devolucion += " string."
        elif aritmeticos.es_operador_aritmetico(lexema):
            devolucion += " operador aritmético."
        elif asignacion.es_operador_asignacion(lexema):
            devolucion += " operador de asignación."
        elif relacionales.es_operador_relacional(lexema):
            devolucion += " operador relacional."
        elif logicos.es_operador_logico(lexema):
            devolucion += " operador lógico."
        elif puntuacion.es_simbolo_de_puntuacion(lexema):
            devolucion += " símbolo de puntuación."
        else:
            devolucion += (" operador que no se utiliza en Python. Error.")
        
        return devolucion
