#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import csv

with open('operaciones.csv', newline='') as csvfile:
    operaciones = csv.reader(csvfile, delimiter=' ', quotechar='')
    for row in operaciones:
        print(row)
