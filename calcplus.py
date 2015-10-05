#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo
import calcoohija


def leer_fichero(fichero):
    lines = fichero.readlines()
    return lines


def calcula_linea(line):
    """Realiza las operaciones que se marcan en cada linea del fichero"""
    operaciones = line.split(',')
    operacion = operaciones[0]
    try:
        funcion = calcoo.dicc[operacion]
    except:
        sys.exit('Operación no válida.')
    operandos = operaciones[1:]
    operandos[-1] = operandos[-1][:-1]
    result = calcoo.numero(operandos[0])
    for operando in operandos[1:]:
        operando1 = calcoo.numero(operando)
        result = calcoo.calculos(funcion, result, operando1)
    return result


def imprimir_resultado(lineas):
    for linea in lineas:
        print(calcula_linea(linea))


if __name__ == "__main__":
    fich = open(sys.argv[1], 'r')
    lines = leer_fichero(fich)
    imprimir_resultado(lines)
