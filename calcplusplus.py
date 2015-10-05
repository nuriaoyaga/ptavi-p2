#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcplus


with open(sys.argv[1]) as fich:
    lines = calcplus.leer_fichero(fich)
    calcplus.imprimir_resultado(lines)
