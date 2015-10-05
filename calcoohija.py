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
            sys.exit("Division by zero is not allowed")


c1 = CalculadoraHija()
#Añadimos al diccionario las nuevas operaciones
calcoo.dicc["producto"] = c1.prod
calcoo.dicc["cociente"] = c1.div


if __name__ == "__main__":
    operando1 = calcoo.numero(sys.argv[1])
    operando2 = calcoo.numero(sys.argv[3])
    print(calcoo.calculos(operando1, operando2))
