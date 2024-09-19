# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:28:25 2024

@author: PC
"""

def recursiv_sum(list_to_sum:list[float])->float:
    if list_to_sum == []:
        return 0
    else:
        return list_to_sum[0] + recursiv_sum(list_to_sum[1:])

def recursiv_fact(nb_int:int)->int:
    if nb_int <= 1:
        return 1
    else:
        return nb_int * recursiv_fact(nb_int-1)
    
def recursiv_len(list_len:list)->int:
    if len(list_len)==0:
        return 0
    else:
        return 1 + recursiv_len(list_len[1:])
    
def recursiv_min(list_min:list[int])->int:
    if len(list_min)==0:
        return ValueError("Error : list is empty")
    elif len(list_min)==1:
        return list_min[0]
    else:
        int_min = recursiv_min(list_min[1:])
        mini = list_min[0]
        if mini > int_min :
            mini = int_min
        return mini

def recursiv_max(list_max:list[int])->int:
    if len(list_max)==0:
        return ValueError("Error : list is empty")
    elif len(list_max)==1:
        return list_max[0]
    else:
        int_max = recursiv_max(list_max[1:])
        maxi = list_max[0]
        if maxi < int_max :
            maxi = int_max
        return maxi
    
def recursiv_pair(list_pair:list[int])->list:
    if len(list_pair)==0:
        return []
    else:
        if list_pair[0]%2==0:
            return [list_pair[0]] + recursiv_pair(list_pair[1:])
        else:
            return recursiv_pair(list_pair[1:])

def recursiv_conc(list_conc:list)->list:
    if len(list_conc)==0:
        return []
    else:
        if list_conc[0] is list:
            while list_conc is list:
                return recursiv_conc(list_conc[0]) + recursiv_conc(list_conc[1:])
        else:
            return list_conc[0] + recursiv_conc(list_conc[1:])
        
def incluse(list_on:list,list_test:list)->bool:
    if list_on:
        res = True
        i = 0
        while res == True and i < len(list_on):
            if list_on[i] not in list_test:
                res = False
            i += 1
    else:
        res = ValueError("Error : empty list ")
    return res
    

def main():
    """
    Point d'entrée du programme.
    """
    void_l = []
    list1 = [1,2,3,4,5,6,7]
    list3 = [6,2,3,7,5,1,4]
    list2 = [2,5,2]
    list4 = [[1,2],[4,5]]
    list5 = [[1,2],[7,[8,9]]]
    list_on1 = [1,2,7]
    list_on2 = [2,4,8,3,5]
    list_test = [1,3,4,2,7,15]
    print("TEST RECURSIV SUM ")
    print("Test with void list : ", recursiv_sum(void_l))
    print("Test with list : [1,2,3,4,5,6,7] : ", recursiv_sum(list1))
    print("-----------------------------")
    print("TEST RECURSIV FACT ")
    print("Test with int 0 : ", recursiv_fact(0))
    print("Test with 10 : ", recursiv_fact(10))
    print("Test with 3 : ", recursiv_fact(3))
    print("-----------------------------")
    print("TEST RECURSIV LEN")
    print("Test with void list : ",recursiv_len(void_l))
    print("Test with list len = 7 : ", recursiv_len(list1))
    print("Test with len = 3 : ", recursiv_len(list2))
    print("-----------------------------")
    print("TEST RECURSIV MIN ")
    print("Test with void list : ",recursiv_min(void_l))
    print("Test with [1,2,3,4,5,6,7] : ", recursiv_min(list3))
    print("Test with [6,2,3,7,5,1,7] : ", recursiv_min(list1))
    print("-----------------------------")
    print("TEST RECURSIV MAX ")
    print("Test with void list : ",recursiv_max(void_l))
    print("Test with [1,2,3,4,5,6,7] : ", recursiv_max(list1))
    print("Test with [6,2,3,7,5,1,7] : ", recursiv_max(list3))
    print("-----------------------------")
    print("TEST RECURSIV PAIR ")
    print("Test with void list : ",recursiv_pair(void_l))
    print("Test with [1,2,3,4,5,6,7] : ", recursiv_pair(list1))
    print("Test with [6,2,3,7,5,1,4] : ", recursiv_pair(list3))
    print("-----------------------------")
    print("TEST RECURSIV CONC ")
    print("Test with void list : ",recursiv_conc(void_l))
    print("Test with [[1,2],[4,5]]: ", recursiv_conc(list4))
    print("Test with [[1,2],[7,[8,9]]] : ", recursiv_conc(list5))
    print("-----------------------------")
    print("TEST INCLUSE ")
    print("Test list_test = [1,3,4,2,7,15] ")
    print("Test with void list : ",incluse(void_l,list_test))
    print("Test with [1,2,7] : ", incluse(list_on1,list_test))
    print("Test with [2,4,8,3,5] : ", incluse(list_on2,list_test))
    print("-----------------------------")
    

if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")