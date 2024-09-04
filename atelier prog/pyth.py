# -*- coding: utf-8 -*-

def affranchissement(choix, poids):
    prix = 0
    if choix == 1:
        if poids <= 20:
            prix = 1.16
        elif poids <= 100:
            prix = 2.32
        elif poids <= 250:
            prix = 4.00
        elif poids <= 500:
            prix = 6.00
        elif poids <= 1000:
            prix = 7.50
        elif poids <= 3000:
            prix = 10.50
        else:
            prix = "string"
    if choix == 2:
        if poids <=20:
            prix = 1.43
            """ code pas fini, même chose et grosse flemme"""
    return prix

start = True
while start:
    print(" Sélectionnez votre choix : \n")
    print("choix 1: lettre verte \nchoix 2: lettre ecopli\nchoix 3: lettre eco outre-mer\nchoix 4:cécogramme")
    choix = input("")
    poids = int(input("Veuillez peser votre lettre : "))
    prix = affranchissement(choix,poids)
    error = True
    while error:
        if 1 <= choix <= 5:
            error = False
        else:
            print("Erreur: veuillez resélectionner \n")
            choix = int(input("choix 1: lettre verte \nchoix 2: lettre ecopli\nchoix 3: lettre eco outre-mer\nchoix 4:cécogramme"))
    if poids is str:
        print("Poids trop lourd, veuillez vous rapprocher d'un employé")
        start = False
    if 1 <= choix <= 3:
        suivi = input("voulez vous un suivi ?\nY/N")
        error = True
        while error:
            if suivi == 'Y':
                prix += 0.50
            elif suivi == 'N':
                prix += 0
            else:
                suivi = input("erreur\n Voulez vous un suivi ?\nY/N")
            error = False
    print("Votre prix à payer est de :",prix)
    start = False
    
    

