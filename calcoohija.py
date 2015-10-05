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


def calculosplus(operacion, op1, op2):
    c1 = CalculadoraHija()
    if operacion == "producto":
        result = c1.prod(op1, op2)
    elif operacion == "cociente":
        result = c1.div(op1, op2)
    else:
        result = calcoo.calculos(operacion, op1, op2)
    return(result)

if __name__ == "__main__":
    operando1 = calcoo.numero(sys.argv[1])
    operando2 = calcoo.numero(sys.argv[3])
    operacion = sys.argv[2]
    print(calculosplus(operacion, operando1, operando2))
