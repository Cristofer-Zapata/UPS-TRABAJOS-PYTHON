# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:41:37 2020

@author: Matiu
"""
matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0],[0,0,0,0,0,0], 
        [0,0,0,0,0,0]]
for i in range(0,5):
    for j in range(0,6):
        print("Ingrese el valor para la posición",i,j)
        matrix[i][j]=int(input())
print(matrix)
