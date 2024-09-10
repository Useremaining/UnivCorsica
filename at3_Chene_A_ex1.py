# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 08:58:11 2024

@author: PC
"""

def full_name(str_name:str)->str:
    """ 
        -- Test of forbidden char in the str --
        -- Two loop, first cut with the detection of a space and different of 0 --
        -- Conversion with ASCII code -- 
        -- ASCII code : A->Z=65->90 and a->z=97->122 --
    """
    if str_name:
        if " " in str_name:
            name_correction = ""
            i = 0
            start = True
            # Loop for the First Name
            while start:
                #cut loop if space detected
                if str_name[i]== " " and i!= 0:
                    start = False
                    name_correction += " "
                # Detection of unconvertible caracter
                elif ord(str_name[i]) < 65 or ord(str_name[i]) > 122 or 90 < ord(str_name[i]) < 97:
                    name_correction = "forbidden caracter in name"
                    start = False
                # if character already in maj, just add
                elif 65 <= ord(str_name[i]) <= 90:
                    name_correction += str_name[i]
                # Else condition is if chr in min -> conversion in MAJ
                else:
                    name_correction += chr(ord(str_name[i])-32)
                i += 1
            start = True
            # Detection of the first letter from Legal Name for conversion
            if ord(str_name[i]) < 65 or ord(str_name[i]) > 122 or 90 < ord(str_name[i]) < 97:
                name_correction = "forbidden caracter in name"
                start = False
            # Test if already in maj
            elif 65 <= ord(str_name[i]) <= 90:
                name_correction += str_name[i]
                i += 1
            else:
                name_correction += chr(ord(str_name[i])-32)
                i += 1
            # Loop for Legal Name conversion
            while start:
                #Cut condition if we're out of str
                if i == len(str_name)-1:
                    start = False
                #Cut if forbidden char
                if ord(str_name[i]) < 65 or ord(str_name[i]) > 122 or 90 < ord(str_name[i]) < 97:
                    start = False
                    name_correction = "forbidden caracter in name"
                # if char is min
                elif 97 <= ord(str_name[i]) <= 122:
                    name_correction += str_name[i]
                # conversion if maj
                else:
                    name_correction += chr(ord(str_name[i])+32)
                i+=1
        else:
            name_correction = "Error : no space"
    else:
        name_correction = None
    return name_correction
    
def test_full_name():
    print("TEST FULL NAME")
    #Fullname name
    fname_lname = "NomENgrAs prEnoMPEtiT"
    void = ""
    forbidden1 = "Hello @world"
    forbidden2 = "Hello wo rld"
    #Test void
    print("Test void : ",full_name(void))
    #Test forbidden caracter @
    print("Test forbidden caracter ",forbidden1," : ",full_name(forbidden1))
    #Test forbidden caracter " "
    print("Test forbidden caracter ",forbidden2," : ",full_name(forbidden2))
    #Test correct name
    print("Conversion of ",fname_lname," : ",full_name(fname_lname))
    print("-----------------------------")

test_full_name()

def is_mail(mail:str)->(int,int):
    """ 
        -- Test if @ in mail --
        -- Then test if . in mail --
        -- Then test if forbidden character --
    """
    if mail:
        #test @ in mail
        if "@" in mail:
            #test if chr before @
            if mail[0] == "@":
                valid = 0
                error = 1
            #test if chr after @
            elif mail[len(mail)-1] == "@":
                valid = 0
                error = 3
            else:
                index_arobase = mail.index("@")
                #test if . in mail
                if "." not in mail[index_arobase:len(mail)]:
                    valid = 0
                    error = 4
                #test if chr before "." or after "."
                elif mail[index_arobase+1] == "." or mail[len(mail)-1] == "." :
                    valid = 0
                    error = 3
                else:
                    valid = 1
                    error = 0
                    authorized_list = [1,2,3,4,5,6,7,8,9,0,"_"]
                    index_point = mail.index(".")
                    """
                        65 = A
                        90 = z
                        97 = a
                        122 = z
                    """
                    for i in range(index_arobase):
                    #test if forbidden chr before @
                        if (ord(mail[i]) < 65 or ord(mail[i]) > 122 or 91 < ord(mail[i]) < 97) and ord(mail[i])not in authorized_list:
                            valid = 0
                            error = 1
                    #test if forbidden chr after @
                    for i in range(index_arobase+1,len(mail)):
                        if (ord(mail[i]) < 65 or ord(mail[i]) > 122 or 91 < ord(mail[i]) < 97) and ord(mail[i])not in authorized_list:
                            if i!= index_point:
                                valid = 0
                                error = 3
        else:
            valid = 0
            error = 2
    else:
        valid = 0
        error = 1
    return (valid,error)

def test_is_mail():
    print("TEST IS MAIL")
    #Fullname name
    mail = "juouujjouu@jjo.fr"
    void = ""
    forbidden1 = "Joaa@."
    forbidden2 = "jooojaz@jek.g[fr"
    no_point = "ijijfij@ejerjr"
    no_arobase = "jeifjiejfzrefjerifj.fr"
    #Test void
    print("Test void : ",is_mail(void))
    #Test forbidden caracter @
    print("Test forbidden caracter ",forbidden1," : ",is_mail(forbidden1))
    #Test forbidden caracter " "
    print("Test forbidden caracter ",forbidden2," : ",is_mail(forbidden2))
    #Test no point
    print("Test no point ",no_point," : ",is_mail(no_point))
    #Test no arobase
    print("Test no arobase ",no_arobase," : ",is_mail(no_arobase))
    #Test correct name
    print("Test correct mail",mail," : ",is_mail(mail))
    print("-----------------------------")
    
test_is_mail()
        
    