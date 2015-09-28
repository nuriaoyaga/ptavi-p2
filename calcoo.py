#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
	def __init__(self, op1, op2):
		self.op1 = op1
		self.op2 = op2

	def plus(self):
		return self.op1 + self.op2

	def minus(self):
		return self.op1 - self.op2


if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
		
	except ValueError:
		sys.exit("Error: Non numerical parameters")

	c1 = Calculadora(operando1, operando2)

	if sys.argv[2] == "suma":
		result = c1.plus()
	elif  sys.argv[2] == "resta":
		result = c1.minus()
	else:
		sys.exit('Operación sólo puede ser sumar o restar.')

	print(result)
	

