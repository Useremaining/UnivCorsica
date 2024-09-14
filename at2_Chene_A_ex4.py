# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:40:34 2024

@author: PC
"""

#----------- Exercice 4 ----------

def val_max(liste:list)->int:
    if len(liste)!=0:
        val_max = liste[0]
        for e in liste:
            if val_max < e:
                val_max = e
    else:
        val_max = None
    return val_max

def val_ind_max(liste:list)->int:
    if len(liste)!=0:
        list_couple=[]
        val_max = liste[0]
        for i in range(len(liste)):
            if val_max <= liste[i]:
                val_max = liste[i]
                ind_max = i
                list_couple.append([val_max,ind_max])
    else:
        liste_couple = None
    return liste_couple

def histo(funct:list)->list:
    """ funct for fonction and hist for histogram
    fonction that return an integer list H that represent the Histogram of an integer list F """
    if funct:
        hist_lst = (val_max(funct)+1)*[0]
        #création d'un dictionnaire pour compter les récurrences
        Dict_Histo = {}
        for i in range(len(funct)):
            hist_lst[funct[i]] +=1
    else:
        hist_lst = []
    return hist_lst
    
def test_histo():
    liste = [6,3,7,8,4,0,9,8,0,0,4,8,10,48,3,0]
    print("TEST HISTO")
    #test liste vide
    print("Test liste vide : ", histo([]))
    #test liste
    print("Test histo avec liste [6,3,7,8,4,0,9,8,0,0,4,8,10,48,3,0]: ", histo(liste))
    print("---------- ----------")

test_histo()

def injectiv(funct:list)->bool: 
    """ fonction that return a bool if the integer list is injectiv """
    if funct:
        hist_lst = histo(funct)
        i = 0
        is_inj = True
        while i < len(hist_lst):
            if hist_lst[i]>1:
                is_inj = False
                i = len(hist_lst)-1
            i += 1
    else:
        is_inj = None
    return is_inj
                
def test_injectiv():
    liste1 = [6,3,7,8,4,0,9,8,0,0,4,8,10,48,3,0]
    liste2 = [1,2,3,4,5]
    print("TEST INJECTIV")
    #test liste vide
    print("Test liste vide : ", injectiv([]))
    #test liste non injectiv
    print("Test liste [6,3,7,8,4,0,9,8,0,0,4,8,10,48,3,0] : ", injectiv(liste1))
    #test liste injectiv
    print("Test liste [1,2,3,4,5] : ", injectiv(liste2))
    print("---------- ----------")
                    
test_injectiv()

def surjectiv(funct:list)->bool:
    """ fonction that return a bool if the integer list is surjectiv"""
    if funct:
        hist_lst = histo(funct)
        i = 0
        is_inj = True
        while i < len(hist_lst):
            if hist_lst[i]==0:
                is_inj = False
                i = len(hist_lst)-1
            i += 1
    else:
        is_inj = None
    return is_inj

def test_surjectiv():
    liste1 = [6,3,7,8,4,0,9,8,0,0,4,8,10,48,3,0] 
    liste2 = [1,2,3,4,5]
    print("TEST SURJECTIV")
    #test liste vide
    print("Test liste vide : ", surjectiv([]))
    #test liste non injectiv
    print("Test liste [6,3,7,8,4,0,9,8,0,0,4,8,10,48,3,0] : ", surjectiv(liste1))
    #test liste injectiv
    print("Test liste [1,2,3,4,5] : ", surjectiv(liste2))
    print("---------- ----------")
    
test_surjectiv()

def bijectiv(funct:list)->bool:
    test = False
    if funct:
        if surjectiv(funct)==True and injectiv(funct)==True:
            test = True
    else:
        test = None
    return test

def test_bijectiv():
    liste1 =  [6,3,7,8,4,0,9,8,0,0,4,8,10,48,3,0]
    liste2 = [0,1,2,3,4,5]
    print("TEST BIJECTIV")
    #test liste vide
    print("Test liste vide : ", bijectiv([]))
    #test liste non injectiv
    print("Test liste  [6,3,7,8,4,0,9,8,0,0,4,8,10,48,3,0] : ", bijectiv(liste1))
    #test liste injectiv
    print("Test liste [0,1,2,3,4,5] : ", bijectiv(liste2))
    print("---------- ----------")
    
test_bijectiv()

def test_histogram(funct:list):
    if funct:
        hist_lst = histo(funct)
        max_value = val_max(hist_lst)
        affichage = "\n"+("  |"*len(hist_lst))
        affichage += "\n"
        while max_value != 0:
            for j in range(len(hist_lst)):
                if hist_lst[j] >= max_value:
                    affichage +=" #|"
                else:
                    affichage += "  |"
            affichage += "\n"
            max_value -= 1
        affichage += "--|"*len(hist_lst)
        affichage += "\n"
        for i in range(len(hist_lst)):
            affichage += " "+str(i)+"|"
        return affichage
    
def test_test_histogram():
    print("HISTOGRAM")
    liste1 = [0,5,5,1,2,5,4,2,2,1,5,5,5,5]
    print("Test liste  [0,5,5,1,2,5,4,2,2,1,5,5,5,5] : ", test_histogram(liste1))
    print("---------- ----------")

test_test_histogram()
            
            