#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:49:03 2021

@author: kevin
"""

notas = []
note = None
counter = 0

while note != "done":
    import numpy as np
    
    note = input("Ingrese la nota del estudiante: ")
    
    if note != "done":
        note = float(note)
        notas.append(note)
        counter += 1
print("El promedio de las notas de los",counter,"estudiantes es:",np.mean(notas))
    
    
    
    
    