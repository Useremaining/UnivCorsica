# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:30:10 2024

@author: PC
"""

#----------- Exercice 3 ----------

""" definition of separation list with negatif number in left, positiv in right, and null in mid """

def separation(lst:list):
    if len(lst) != 0:
        LSEP = []
        negativ = []
        null = []
        positiv = []
        for elt in lst:
            if elt <0:
                negativ.append(elt)
            elif elt > 0:
                positiv.append(elt)
            else:
                null.append(elt)
        for i in range(len(negativ)):
            LSEP.append(negativ[i])
        for i in range(len(null)):
            LSEP.append(null[i])
        for i in range(len(positiv)):
            LSEP.append(positiv[i])
    else:
        LSEP = None
    return LSEP

def test_separation():
    liste = [-6,3,7,8,-4,0,9,8,0,0,-4,8,10,48,-3,0]
    print("TEST POSITION TRI")
    #test liste vide
    print("Test liste vide : ", separation([]))
    #test liste
    print("Test separation avec liste : [-6,3,7,8,-4,0,9,8,0,0,-4,8,10,48,-3,0] : ", separation(liste))
    print("---------- ----------")
    
test_separation()
    