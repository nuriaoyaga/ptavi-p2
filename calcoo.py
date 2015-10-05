#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys


class Calculadora():

    def plus(self, op1, op2):
    #Operacion suma
        return op1 + op2

    def minus(self, op1, op2):
    #Operacion resta
        return op1 - op2


def numero(op):
    """Funcion que pasa de string a float o int"""
    try:
        if '.' in op:
            return(float(op))
        else:
            return(int(op))
    except ValueError:
        sys.exit("Error: Non numerical parameters")


def crear_operaciones(arg):
    pass


c1 = Calculadora()
#creamos un diccionario con las operaciones y su funcion
dicc = {"suma": c1.plus, "resta": c1.minus}


def calculos(funcion, operando1, operando2):
    """Funcion que realiza los calculos segun la clave del diccionario"""
    result = funcion(operando1, operando2)
    return result


if __name__ == "__main__":
    operando1 = numero(sys.argv[1])
    operando2 = numero(sys.argv[3])
    try:
        funcion = dicc[sys.argv[2]]
    except:
        sys.exit('Operación no válida.')
    print(calculos(funcion, operando1, operando2))
