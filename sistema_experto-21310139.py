# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:12:54 2024

@author: moy  logica pag 224 sistemas expertos: un enfoque moderno
"""

#Hoy es lunes y está lloviendo, o voy al trabajo. y hay tráfico en la carretera o no llego a tiempo, pero y puede ser que llego a tiempo y está lloviendo

import re
import string
from os import system

import matplotlib.pyplot as plt


# Operadores booleanos
operadores = {
    'y': '∧',   # "y" se convierte en "^" (AND)
    'o': '∨',   # "o" se convierte en "v" (OR)
    'no': '~',   # "no" se convierte en "~" (NOT)
}


class Nodo:
    def __init__(self, valor=None, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def generar_arbol_binario(n, nivel=0):
    if nivel == n:
        return None
    nodo = Nodo(valor=f'X{nivel+1}')
    nodo.izquierda = generar_arbol_binario(n, nivel + 1)
    nodo.derecha = generar_arbol_binario(n, nivel + 1)
    return nodo

def imprimir_arbol(nodo, nivel=0):
    if nodo is not None:
        imprimir_arbol(nodo.derecha, nivel + 1)
        print(' ' * 4 * nivel + '->', nodo.valor)
        imprimir_arbol(nodo.izquierda, nivel + 1)




def imprimir_tabla_binaria(n):
    # Número total de combinaciones posibles (2^n)
    total_combinaciones = 2 ** n
    
    # Encabezado de la tabla
    encabezado = [f'X{i+1}' for i in range(n)]
    print('\t'.join(encabezado))

    # Generar y mostrar cada combinación en binario
    for i in range(total_combinaciones):
        # Convertir a binario y rellenar con ceros a la izquierda hasta tener longitud n
        binario = format(i, f'0{n}b')
        # Imprimir cada bit separado por tabuladores
        print('\t'.join(binario))


def procesar_texto(texto):
    n = 0
    

    # Divide el texto usando los operadores lógicos como separadores
    partes = re.split(r'\s+(y|o|no)\s+', texto)

    # Inicializa diccionario para almacenar las oraciones
    oraciones = {}
    operador_actual = []
    
    # Asignar oraciones a variables (a, b, c, ...)
    variable_index = 0
    for i, parte in enumerate(partes):
        # Si la parte actual es un operador, lo almacenamos
        if parte in operadores:
            operador_actual.append(operadores[parte])
        else:
            # Elimina espacios extra de la oración
            oracion = parte.strip()
            if oracion:
                # Asigna la oración a una variable en orden alfabético
                variable = string.ascii_lowercase[variable_index]
                oraciones[variable] = oracion
                variable_index += 1
                n = variable_index

    # Construye la expresión lógica con paréntesis para agrupar correctamente
    expresion = ""
    variable_index = 0
    aplicar_no = False  # Para indicar si el próximo término debe ser negado
    operador_anterior = None  # Para manejar operadores consecutivos
    for i, parte in enumerate(partes):
        if parte in operadores:
            # Maneja operadores y agrupa correctamente con paréntesis
            if parte == "y":
                expresion += " ∧ "
            elif parte == "o":
                expresion += " ∨ "
            elif parte == "no":
                aplicar_no = True  # La siguiente variable será negada
                operador_anterior = parte  # Marca el operador encontrado
        else:
            # Evita que se tomen espacios vacíos o textos que sean operadores consecutivos
            if parte.strip() and operador_anterior != parte:
                variable = string.ascii_lowercase[variable_index]  #f"X{n}"
                # Si hay un "no" antes, agrega el símbolo de negación
                if aplicar_no:
                    expresion += f"~{variable}"
                    aplicar_no = False  # Resetea el indicador
                else:
                    expresion += variable
                variable_index += 1
                operador_anterior = None  # Reinicia el operador anterior para la siguiente iteración

    # Muestra los resultados
    print("Oraciones asignadas a variables:\ny = and(^)\to = or(v)\tno = not(~)\n\n", entrada, "\n\nTabla de atomos:")
    for var, oracion in oraciones.items():
        print(f"{var} = {oracion}")
    
    print("\nExpresión lógica resultante:")
    print(expresion, "\n\nTabla de verdad: \n")
    imprimir_tabla_binaria(n)
    
    
    
    arbol = generar_arbol_binario(n)
    imprimir_arbol(arbol)
    
    return partes
    
    

# Ejemplo de uso
entrada = input("Frase: ")
#system('cls')
proposiciones_simples = procesar_texto(entrada)

