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
    #pasa a entero o a float
    try:
        if '.' in op:
            return(float(op))
        else:
            return(int(op))
    except ValueError:
        sys.exit("Error: Non numerical parameters")

def calculos (operacion, operando1, operando2):
    c1 = Calculadora()
    if operacion == "suma":
        result = c1.plus(operando1, operando2)
    elif operacion == "resta":
        result = c1.minus(operando1, operando2)
    else:
        sys.exit('Operación no válida.')
    return result


if __name__ == "__main__":
    operando1 = numero(sys.argv[1])
    operando2 = numero(sys.argv[3])
    operacion = sys.argv[2]
    print(calculos (operacion, operando1, operando2))
