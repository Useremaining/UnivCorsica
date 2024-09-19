# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:00:04 2024

@author: PC
"""

import numpy as np

def searchsorted(table:object,num:int)->int:
    i = 0
    while i < len(table) and table[i] != num:
        i +=1
    return i

def my_where(table:object,num:int)->int:
    i = 0
    j = 0
    while i < table.shape[0]:
        while j < table.shape[1]:
            print(i,j)
            if num == table[i][j]:
                return i,j
            j+=1
        i += 1
        j = 0
    else:
        return ValueError("This number is not in the table")
    
def add_v1(tab1:object,tab2:object)->object:
    if tab1.shape == tab2.shape:
        res = np.zeros(tab1.shape)
        for i,x in np.ndenumerate(tab1):
            res[i]=tab1[i]+tab2[i]
        return res
    else:
        return ValueError("Warning ! Dim are not even ")

def add_v2(tab1:object,tab2:object)->object:
    if tab1.shape == tab2.shape:
        res = np.zeros(tab1.shape)
        for i in range(tab1.shape[0]):
            for j in range(tab2.shape[1]):
                res[i][j]=tab1[i][j]+tab2[i][j]
        return res
    else:
        return ValueError("Warning ! Dim are not even ")

def main():
    """
    Entry program.
    """
    tabl = np.array([2,4,5,6,7])
    a = np.array([[1,4,5,6],[2,3,7,8]])
    dim3_1 = np.array([[1,2,4,5],[13,5,7,8],[9,5,7,3]])
    dim3_2 = np.array([[2,4,7,8],[5,64,12,3],[45,4,9,0]])
    print("TEST SEARCHSORTED")
    print("test avec [2,4,5,6,7] et 5 : ",searchsorted(tabl, 5))
    print("-----------------------------")
    print("TEST MY WHERE")
    print("test avec [[1,4,5,6],[2,3,7,8]] et 7 : ", my_where(a,7))
    print("test avec [[1,4,5,6],[2,3,7,8]] et 7 : ", my_where(a,5))
    print("-----------------------------")
    print("TEST ADD V1 ET V2")
    print("test V1 : ", add_v1(dim3_1,dim3_2))
    print("test V1 : ", add_v2(dim3_1,dim3_2))
    print("-----------------------------")
        
if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")