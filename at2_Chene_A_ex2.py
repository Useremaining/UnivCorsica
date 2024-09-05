# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:26:25 2024

@author: PC
"""

#----------- Exercice 2 ----------

""" définition de la position d'indice d'un élément d'une liste """

def position1(lst:list,elt:int)->int:
    if elt not in lst:
        elt= -1
    else: 
        for i in range(len(lst)):
            if elt == lst[i]:
                elt = i
    return elt
    
def position2(lst:list,elt:int)->int:
    e = -1
    i = 0
    while elt in lst:
        if elt == lst[i]:
            e = i
            elt = None
        else:
            i+=1
    return e

def test_position():
    #création d'une liste
    l = [4,2,30,8,12]
    print("TEST POSITION 1")
    #test liste vide
    print("Test liste vide : ", position1([],0))
    #test liste 1
    print("Test position1 élément non présent : ", position1(l,3))
    #test liste 2
    print("Test position1 élément présent : ", position1(l,12))
    print("---------- ----------")
    print("TEST POSITION 2")
    #test liste vide
    print("Test liste vide : ", position2([],0))
    #test liste 1
    print("Test position2 élément non présent : ", position2(l,3))
    #test liste 2
    print("Test position2 élément présent : ", position2(l,12))
    print("---------- ----------")

test_position()

""" définition du nombre d'occurence d'un entier dans une liste d'entiers """

def nb_occurrence(lst:list,e:int)->int:
    count = 0
    """ si e n'est pas dans la liste, aucune boucle"""
    if e in lst:
        for elt in lst:
            if e == elt:
                count +=1
    return count

def test_nb_occurrence():
    #création d'une liste
    l = [4,2,30,8,12,12,12,12]
    print("TEST NB OCCURENCE")
    #test liste vide
    print("Test liste vide : ", nb_occurrence([],7))
    #test liste 1
    print("Test occurrence élément non présent : ", nb_occurrence(l,3))
    #test liste 2
    print("Test position1 élément présent : ", nb_occurrence(l,12))
    print("---------- ----------")

test_nb_occurrence()

""" définition booléenne si une liste est triée par ordre croissant ou non """

def est_triee(lst)->bool:
    test = True
    if len(lst) == 0:
        test = False
    else:
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                test = False
                break
    return test

def est_triee_while(lst)->bool:
    test = True
    if len(lst) == 0:
        test = False
    else:
        i = 0
        while i != len(lst)-1:
            i += 1
            if lst[i-1] > lst[i]:
                i=len(lst)-1
                test = False
    return test

def test_est_triee():
    #création d'une liste
    l = [4,2,30,8,12,12,12,12]
    ltriee = [1,2,3,4,5,6,7,8,9,10]
    print("TEST EST_TRIEE")
    #test liste vide
    print("Test liste vide : ", est_triee([]))
    #test liste 1
    print("Test est triee 4,2,30,8,12,12,12,12 ", est_triee(l))
    #test liste 2
    print("Test est triee 1,2,3,4,5,6,7,8,9,10 : ", est_triee(ltriee))
    print("---------- ----------")
    print("TEST EST_TRIEE_WHILE")
    #test liste vide
    print("Test liste vide : ", est_triee_while([]))
    #test liste 1
    print("Test est triee 4,2,30,8,12,12,12,12 ", est_triee_while(l))
    #test liste 2
    print("Test est triee 1,2,3,4,5,6,7,8,9,10 : ", est_triee_while(ltriee))
    print("---------- ----------")

test_est_triee()
        
""" définition d'une recherche dichotomique """

def position_tri(lst:list,elt:int)->int:
    if est_triee_while(lst) is True:
        """ création début et fin qui permettrons de parcourir la liste """
        fin = len(lst)
        debut = 0
        """ i est l'index qui parcoura la liste"""
        if fin%2==0:
            i = fin/2
            print("pair ",i)
        else:
            i = int(((fin-1)/2)+1)
            print("impaire ",i)
        start = True
        fin -= 1
        while start:
            if elt > lst[i]:
                i = fin
                fin -= 1
            elif elt < lst[i]:
                i = debut
                debut += 1
            else:
                start = False
    else:
        i=None
    return i

def test_position_tri():
    liste1 = [1,2,3,4,5,6,7,8,9,10,11]
    liste2 = [1,2,3,4,5,6,7,8,9,10,11]
    print("TEST POSITION TRI")
    #test liste vide
    print("Test liste vide : ", position_tri([],5))
    #test liste 1
    print("Test position 3 avec [1,2,3,4,5,6,7,8,9,10] : ", position_tri(liste1,3))
    #test liste 2
    print("Test position 6 avec [1,2,3,4,5,6,7,8,9,10,11] : ", position_tri(liste2,6))
    print("---------- ----------")

test_position_tri()

""" définition de la répétition d'un entier dans une liste """

"""def a_repetition(lst:list)->bool:
    repetition = False
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:
                repetition = True
                break
    return repetition"""

def a_repetition(lst:list)->bool:
    repetition = False
    if len(lst)!=0:
        i = 0
        j = 1
        while i != len(lst):
            search = lst[i]
            while j != len(lst):
                if search == lst[j]:
                    repetition = True
                    j = len(lst)-1
                j += 1
            if repetition == True:
                i = len(lst)-1
            i+=1
            j=i+1
        return repetition

def test_position_tri():
    liste1 = [1,2,3,4,5,6,7,8,9,10]
    liste2 = [1,2,3,4,5,6,7,8,9,10,10]
    print("TEST A_REPETITION ")
    #test liste vide
    print("Test liste vide : ", a_repetition([]))
    #test liste 1
    print("Test 3 avec [1,2,3,4,5,6,7,8,9,10] : ", a_repetition(liste1))
    #test liste 2
    print("Test 10 avec [1,2,3,4,5,6,7,8,9,10,10] : ", a_repetition(liste2))
    print("---------- ----------")
    
test_position_tri()