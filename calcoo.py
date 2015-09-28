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


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    c1 = Calculadora()

    if sys.argv[2] == "suma":
        result = c1.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = c1.minus(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
