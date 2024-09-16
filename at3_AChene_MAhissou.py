# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:49:12 2024

@author: PC
"""
import sys

def word_nLetters(lst_words:list,n:int)->list:
    """ return a string list where the word in the other list as a len of n """
    words = []
    if lst_words:
        if n > 1:
            for e in lst_words:
                if len(e) == n:
                    words.append(e)
        else:
            words = ["n too small"]
    else:
        words = ["No word in list"]
    return words

def start_with(words:str,prefix:str)->bool:
    """
        Return True if the words start with the prefix, and False if not
    """
    if words:
        if prefix or len(prefix)>=len(words):
            if prefix in words[:len(prefix)]:
                result = True
                
            else:
                result = False
        else:
            result = "Error : no prefix"
    else:
        result = "Error : no word"
    return result
    
def end_with(words:str,suffix:str)->bool:
    """
        Return True if the words end with the suffix, False if not
    """
    if words:
        if suffix or len(suffix)>=len(words):
            if suffix in words[len(words)-len(suffix):len(words)]:
                result = True
            else:
                result = False
        else:
            result = "Error suffix"
    else:
        result="Error : no word"
    return result

def list_end_with(lst_words:list,suffix:str)->list:
    if lst_words:
        if suffix:
            #List word in correspondance with suffix
            lst_wrd_sfx = []
            for elt in lst_words:
                if end_with(elt,suffix):
                    lst_wrd_sfx.append(elt)
        else:
            lst_wrd_sfx = [" Error : no suffix "]
    else:
        lst_wrd_sfx = ["Error : no word"]
    return lst_wrd_sfx

def list_start_with(lst_words:list,prefix:str)->list:
    if lst_words:
        if prefix:
            lst_wrd_pfx = []
            for elt in lst_words:
                if start_with(elt, prefix):
                    lst_wrd_pfx.append(elt)
        else:
            lst_wrd_pfx = [" Error : no prefix "]
    else:
        lst_wrd_pfx = ["Error : no word "]
    return lst_wrd_pfx

def dictionnary(file)->list:
    open_file = open("littre.txt","r")
    lst_file = []
    c = open_file.readline()
    while c!= "":
        lst_file.append(c)
        c = open_file.readline()
    return lst_file

def main():
    """
    Point d'entrée du programme.
    """
    print("TEST MOT N LETTRES")
    #Fullname name
    lst_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour","finir", "aimer"]
    void = []
    #Test void
    print("Test void : ",word_nLetters(void,5))
    #Test forbidden caracter @
    print("List is : jouer, bonjour, punir, jour, aurevoir, revoir, pouvoir, cour, abajour, finir, aimer")
    print("Test with n = 4 : ",word_nLetters(lst_mot, 4))
    print("Test with n = 7 : ",word_nLetters(lst_mot, 7))
    #Test forbidden caracter " "
    print("-----------------------------")
    print("TEST START WITH")
    print("void : ",start_with("erer",""))
    print("Test avec Bonjour et bon : ", start_with("bonjour","bon"))
    print("Test avec Bonjour et bin : ", start_with("bonjour","bin"))
    print("-----------------------------")
    print("TEST END WITH")
    print("void : ",end_with("","zeze"))
    print("Test avec Bonjour et our : ", end_with("bonjour","our"))
    print("Test avec Bonjour et por : ", end_with("bonjour","por"))
    print("-----------------------------")
    print("TEST LIST END WITH")
    print("void : ",list_end_with([],""))
    print("Test previous list with our : ", list_end_with(lst_mot,"our"))
    print("Test previous list with por : ", list_end_with(lst_mot,"por"))
    print("-----------------------------")
    print("TEST LIST START WITH WITH")
    print("void : ",list_end_with([],""))
    print("Test previous list with our : ", list_start_with(lst_mot,"jou"))
    print("Test previous list with por : ", list_start_with(lst_mot,"por"))


if __name__ == "__main__":
    print("Le script est exécuté directement.")
    main()
else:
    print("Le script est importé comme un module.")
