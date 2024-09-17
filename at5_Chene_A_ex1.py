# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:44:44 2024

@author: PC
"""
import random as rand
import time
import matplotlib.pyplot as plt
import numpy as np

#pas capté le truc à refaire (3 paramètre)
def gen_list_random_int(para_int:int=0)->list[int]:
    list_rand_int = []
    if para_int:
        for i in range(para_int):
            list_rand_int.append(rand.randint(-2^32,2^32))
    else:
        for i in range(0,10):
            list_rand_int.append(rand.randint(0,10))
    return list_rand_int

def mix_list(list_to_mix:list)->list:
    if list_to_mix:
        mixed_list = []
        exclued = []
        while len(mixed_list)!=len(list_to_mix):
            value = rand.randint(0,len(list_to_mix)-1)
            if value not in exclued:
                mixed_list.append(list_to_mix[value])
                exclued.append(value)
    else:
        mixed_list=["Error"]
    return mixed_list
"""
def mix_list_ver2(list_to_mix:list)->list:
    mixed_list = list_to_mix.copy()
    if len(list_to_mix)<10:
        cut = 1
    else:
        if len(list_to_mix)%10 != 0:
            cut = (len(list_to_mix)//10)+1
        else:
            cut = len(list_to_mix)//10
    for i in range(cut):"""
        
        
def random_pick_list(list_element:list)->all:
    if list_element:
        index = rand.randint(0,len(list_element)-1)
    else:
        list_element.append("error")
        index = 0
    return list_element[index]

def mult_random_pick_list(list_element:list,nb_pick:int)->list:
    if list_element:
        if nb_pick >= 1 and nb_pick <= len(list_element):
            return_list = []
            exclued_list = []
            while nb_pick:
                rng = random_pick_list(list_element)
                if rng not in exclued_list:
                    return_list.append(rng)
                    exclued_list.append(rng)
                    nb_pick -=1
        else:
            return_list = ["Error number "]
    else:
        return_list = ["Error void list "]
    return return_list

def perf_mix(fct1:callable(list),fct2:callable(list),list_test:list[int],nb_exe:int)->tuple:
    """
    Parameters
    ----------
    fct1 : callable([],list)
        THIS FUNCTION NEED TO RETURN A LIST
    fct2 : callable([],list)
        THIS FUNCTION NEED TO RETURN A LIST
    list_test : list[int]
        THIS LIST CONTAIN THE LARGE OF LIST CREATED FOR TEST
    nb_exe : int
        NUMBER OF EXECUTION TIME
    
    Returns
    -------
    tuple
        RETURN AVERAGE TIME FROM EACH FUNCTION TO EXECUTE THE CODE
    """
    #test one :
    average_time_fct1 = 0
    average_time_fct2 = 0
    for i in range(len(list_test)):
        gen_list = gen_list_random_int(list_test[i])
        # utilisation function 1
        start_pc = time.perf_counter()
        for j in range(nb_exe):
            fct1(gen_list)
        end_pc = time.perf_counter()
        elapsed_time_pc = end_pc - start_pc
        average_time_fct1 += elapsed_time_pc
        print("FCT1 _ Résultat pour la taille de liste : ",list_test[i],"\n temps écoulé : ",elapsed_time_pc,"\n ---- ")
        #
        start_pc = time.perf_counter()
        for j in range(nb_exe):
            fct2(gen_list)
        end_pc = time.perf_counter()
        elapsed_time_pc = end_pc - start_pc
        average_time_fct2 += elapsed_time_pc
        print("FCT2 _ Résultat pour la taille de liste : ",list_test[i],"\n temps écoulé : ",elapsed_time_pc,"\n ---- ")
    average_time_fct1 = average_time_fct1 / (len(list_test)*nb_exe)
    return ["Execute time function 1 : ",average_time_fct1],[" Execute time function 2 : ",average_time_fct2]
    
def main():
    """
    Point d'entrée du programme.
    """
    list1 = [-34, -19, -32, 14, 18, 33, -17, 20, -18, -32, -30, -21, -20, 14, 27, -27, 9, 21, 5, -31]
    list2 = [10,100,1000]
    print("TEST GEN LIST RANDOM INT ")
    print("Test vide : ", gen_list_random_int())
    print("Test avec 20 : ", gen_list_random_int(20))
    print("-----------------------------")
    print("TEST MIXED LIST ")
    print("Test void : ", mix_list([]))
    print("Test with [-34, -19, -32, 14, 18, 33, -17, 20, -18, -32, -30, -21, -20, 14, 27, -27, 9, 21, 5, -31] : \n",mix_list(list1))
    print("Test bis : \n", mix_list(list1))
    print("-----------------------------")
    print("TEST RANDOM PICK LIST ")
    print("Test void : \n", random_pick_list([]))
    print("Test with [-34, -19, -32, 14, 18, 33, -17, 20, -18, -32, -30, -21, -20, 14, 27, -27, 9, 21, 5, -31] :\n",random_pick_list(list1))
    print("Test bis : \n",random_pick_list(list1))
    print("-----------------------------")
    print("Test MULT RANDOM PICK LIST ")
    print("Test void list : ", mult_random_pick_list([],3))
    print("Test number < 1 : ", mult_random_pick_list(list1, 0))
    print("Test same list with 3 : \n",mult_random_pick_list(list1, 3))
    print("Test same list with 300 : \n ",mult_random_pick_list(list1, 300))
    print("-----------------------------")
    print("TEST PERF MIX ")
    print(perf_mix(mix_list,rand.shuffle,list2,1))
    
    
if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")