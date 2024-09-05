# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:27:44 2024

@author: PC
"""

#----------- Exercice 1 ----------

""" définition des sommes """
def somme1(liste:list)->int:
    somme = 0
    for i in range(len(liste)):
        somme += liste[i]
    return somme

def somme2(liste:list)->int:
    somme = 0
    for e in liste:
        somme += e
    return somme

def somme3(liste:list)->int:
    somme = 0
    i = 0
    while i < len(liste):
        somme += liste[i]
        i += 1
    return somme

def test_exercice1 ():
    print("TEST SOMME1")
    #test liste vide
    print("Test liste vide : ", somme1([]))
    #test somme 11111
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", somme1(lst2test1))
    print("---------- ----------")
    print("TEST SOMME2")
    #test liste vide
    print("Test liste vide : ", somme2([]))
    #test somme 11111
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", somme2(lst2test1))
    print("---------- ----------")
    print("TEST SOMME3")
    #test liste vide
    print("Test liste vide : ", somme3([]))
    #test somme 11111
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", somme3(lst2test1))
    print("---------- ----------")

test_exercice1()

""" definition de la moyenne d'une liste d'entier """

def moyenne(liste:list)->float:
    denominateur = len(liste)
    if not liste:
        moyenne = 0
    else:
        moyenne = somme2(liste) / denominateur
    return moyenne

def test_moyenne():
    print("TEST MOYENNE")
    #test liste vide
    print("Test liste vide : ", moyenne([]))
    #test liste 1
    print("Test moyenne 1,7,10,113,91,3 : ", moyenne([1,7,10,113,91,3]))
    #test liste 2
    print("Test moyenne 10,111,2003,2929 : ", moyenne([10,111,2003,2929]))
    print("---------- ----------")

test_moyenne()

""" définition des nombres supérieurs à l'entier donné """

def nb_sup1(liste:list,e:int)->list:
    liste_sup = []
    for i in range(len(liste)):
        if e < liste[i]:
            liste_sup.append(liste[i])
    return liste_sup

def nb_sup2(liste:list,e:int)->list:
    liste_sup = []
    for element in liste:
        if e < element:
            liste_sup.append(element)
    return liste_sup

def test_nb_sup():
    print("TEST NB_SUP1")
    #test liste vide
    print("Test liste vide : ", nb_sup1([],0))
    #test liste 1
    print("Test nb_sup1 1,7,10,113,91,3 avec 20 : ", nb_sup1([1,7,10,113,91,3],20))
    #test liste 2
    print("Test nb_sup1 10,111,2003,2929 avec 333 : ", nb_sup1([10,111,2003,2929],333))
    print("---------- ----------")
    print("TEST NB_SUP2")
    #test liste vide
    print("Test liste vide : ", nb_sup1([],0))
    #test liste 1
    print("Test nb_sup2 1,7,10,113,91,3 avec 20 : ", nb_sup2([1,7,10,113,91,3],20))
    #test liste 2
    print("Test nb_sup2 10,111,2003,2929 avec 333 : ", nb_sup2([10,111,2003,2929],333))
    print("---------- ----------")

test_nb_sup()

""" définition de la moyenne des valeurs supérieures à un entier donné """

def moy_sup(liste:list,e:int)->float:
    return moyenne(nb_sup2(liste,e))

def test_moy_sup():
    print("TEST MOY_SUP")
    #test liste vide
    print("Test liste vide : ", moy_sup([],0))
    #test liste 1
    print("Test moy_sup 1,7,10,113,91,3 avec 20 : ", moy_sup([1,7,10,113,91,3],20))
    #test liste 2
    print("Test moy_sup 10,111,2003,2929 avec 333 : ", moy_sup([10,111,2003,2929],333))
    print("---------- ----------")
    
test_moy_sup()

""" définition de la valeur maximale d'une liste d'entiers """

def val_max(liste:list)->int:
    if len(liste)!=0:
        val_max = liste[0]
        for e in liste:
            if val_max < e:
                val_max = e
    else:
        val_max = None
    return val_max

def test_val_max():
    print("TEST VAL_MAX")
    #test liste vide
    print("Test liste vide : ", val_max([]))
    #test liste 1
    print("Test val_max 1,7,10,113,91,3 avec 20 : ", val_max([1,7,10,113,91,3]))
    #test liste 2
    print("Test val_max 10,111,2003,2929 avec 333 : ", val_max([10,111,2003,2929]))
    print("---------- ----------")
    
test_val_max()

""" définition de l'indice de la valeur maximale d'une liste d'entiers"""

def ind_max(liste:list)->int:
    val_max = 0
    ind_max = None
    for i in range(len(liste)):
        if val_max < liste[i]:
            val_max = liste[i]
            ind_max = i
    return ind_max

def test_ind_max():
    print("TEST IND_MAX")
    #test liste vide
    print("Test liste vide : ", ind_max([]))
    #test liste 1
    print("Test ind_max 1,7,10,113,91,3 avec 20 : ", ind_max([1,7,10,113,91,3]))
    #test liste 2
    print("Test ind_max 10,111,2003,2929 avec 333 : ", ind_max([10,111,2003,2929]))
    print("---------- ----------")
    
test_ind_max()

#----------- Exercice 2 ----------

#----------- Exercice 3 ----------

#----------- Exercice 4 ----------

#----------- Exercice 5 ----------

#----------- Exercice 6 ----------