#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import calcoo


class CalculadoraHija(calcoo.Calculadora):
    #operacion producto
    def prod(self, op1, op2):
        return op1 * op2

    def div(self, op1, op2):
    #Operacion division
        try:
            return op1 / op2
        except ZeroDivisionError:
            print("Division by zero is not allowed")

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    c1 = CalculadoraHija()

    if sys.argv[2] == "producto":
        result = c1.prod(operando1, operando2)
    elif sys.argv[2] == "cociente":
        result = c1.div(operando1, operando2)
    elif sys.argv[2] == "suma":
        result = c1.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = c1.minus(operando1, operando2)
    else:
        sys.exit('Operación no válida.')

    print(result)
