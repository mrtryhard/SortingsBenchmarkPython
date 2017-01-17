#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Tri par tas (heapsort)
# lst : Liste d'entier à trier. 
def tri_par_tas(lst):
    # Converti la liste en tas 
    taille = len( lst ) - 1
    petit_parent = taille // 2
    # range: [taille, -1[, iterateur -= 1 
    # itération taille -> -1 (exclu)
    for i in range (petit_parent, -1, -1 ):
        tassifier(lst, i, taille)
 
    # Applati le tas en tableau trié. 
    # range: [taille, 0[, iterateur -= 1
    # itération taille -> 0 (exclu)
    for i in range(taille, 0, -1):
        if lst[0] > lst[i]:
            # Swap 
            lst[0], lst[i] = lst[i], lst[0]
            tassifier(lst, 0, i-1)
    
    return lst
 
# S'assure que la structure est un tas. 
def tassifier(lst, premier, dernier):
    plus_grand = 2 * premier + 1
    while plus_grand <= dernier:
        # Si l'enfant de droite existe et plus grand que l'enfant de gauche... 
        if (plus_grand < dernier) and (lst[plus_grand] < lst[plus_grand + 1]):
            plus_grand += 1
 
        # L'enfant de droite est plus grand que le parent...
        if lst[plus_grand] > lst[premier]:
            # Swap 
            lst[plus_grand],lst[premier] = lst[premier],lst[plus_grand]
            
            # Descend jusqu'à l'enfant le plus grand.
            premier = plus_grand;
            plus_grand = 2 * premier + 1
        else:
            # On a plus a tassifier. 
            return 

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Requires list.")
    else:
        list_of_integers = [int(i) for i in sys.argv[1:]]
     
        lst = tri_par_tas(list_of_integers)
    
        print("Sorted List: ")
        print(lst)
        print("Heap sort end.")