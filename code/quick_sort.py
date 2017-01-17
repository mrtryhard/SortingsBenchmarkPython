#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Tri Rapide (Quicksort)
# lst : Liste à trier. 
def tri_rapide(lst):
    tri_rapide_rec(lst, 0, len(lst)-1)
 
def tri_rapide_rec(lst, gauche, droite):
    temp_stack = []
    temp_stack.append((gauche, droite))
    
    while temp_stack:      
        pos = temp_stack.pop()
        droite, gauche = pos[1], pos[0]
        pivot = partition(lst, gauche, droite)
        
        # Si les items à la gauche du pivot, alors on les mets dans le stack
        if (pivot - 1) > gauche:
            temp_stack.append((gauche, pivot - 1))
            
        #Si des items à droite du pivot on les pushs dans le stack.
        if (pivot + 1) < droite:
            temp_stack.append((pivot + 1, droite))            
       
# Partitionne la liste en entrée en 2 partitions en trouvant un pivot. 
# lst : liste à trier
# premier : Borne de gauche de la liste de gauche 
# dernier : Borne de droite de la liste de droite
def partition(lst, premier, dernier):
    pivot = lst[premier]

    gauche = premier + 1
    droite = dernier
    
    est_complet = False
    while not est_complet:

        while gauche <= droite and lst[gauche] <= pivot:
            gauche = gauche + 1
     
        while lst[droite] >= pivot and droite >= gauche:
            droite = droite -1
     
        if droite < gauche:
            est_complet = True
        else:
            # Swap 
            lst[gauche], lst[droite] = lst[droite], lst[gauche]
    
    # Swap 
    lst[premier], lst[droite] = lst[droite], lst[premier]
    
    return droite
   
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Requires list.")
    else:
        list_of_integers = [int(i) for i in sys.argv[1:]]
     
        tri_rapide(list_of_integers)
    
        print("Sorted List: ")
        print(list_of_integers)
        print("Quick sort end.")