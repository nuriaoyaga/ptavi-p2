#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import calcoohija

fich = open('operaciones','r')
lines = fich.readlines() #crea una lista con las lineas del fichero

if __name__ == "__main__":
    for line in lines:
        operaciones = line.split(',')
        operacion = operaciones[0]
        operandos = operaciones[1:]
        operandos[-1] = operandos[-1][:-1]
        c1 = calcoohija.CalculadoraHija()
        result = int(operandos[0])
        if operacion == "suma":
            for operando in operandos[1:]:
                operando = c1.numero(operando)    
                result = c1.plus(result, operando)
        elif operacion == "resta":
            for operando in operandos[1:]:
                operando = c1.numero(operando)   
                result = c1.minus(result, operando)   
        elif operacion == "divide":
            for operando in operandos[1:]:
                operando = c1.numero(operando)   
                result = c1.div(result, operando)  
        elif operacion == "multiplica":
            for operando in operandos[1:]:
                operando = c1.numero(operando)   
                result = c1.prod(result, operando)    
        else:
            sys.exit('Operación no válida.')

        print(result)
  



