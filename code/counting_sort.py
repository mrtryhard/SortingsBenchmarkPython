#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Tri comptage. 
# lst : liste d'entier 
# k   : valeur maximale
# -----
# Change la liste reçu en paramètres avec la liste triée.
def tri_comptage(lst, k):
    # Initialisation du tableau de dimension k + 1 (pour gérer le cas 0)
    lst_compte = [0 for i in range(k + 1)]
    
	# Pour chaque entier dans la liste, on incrémente son occurence.
    for i in lst:
        lst_compte[i] += 1

    # On reconstruit la liste in-place en ordre naturelle.
    pos_in_lst = 0;
    j = 0
    while j < (k + 1):
        # Tant qu'on a pas placé tous les nombre d'élément de lst_compte[j].
        while 0 < lst_compte[j]:
            lst[pos_in_lst] = j
            pos_in_lst += 1
            lst_compte[j] -= 1
        j += 1
    
    # Retourne lst. 
    return lst

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Requires list.")
    else:
        list_of_integers = [int(i) for i in sys.argv[1:]]
        max_int = max(list_of_integers)
     
        lst = tri_comptage(list_of_integers, max_int)
    
        print("Sorted List: ")
        print(lst)
        print("Counting sort end.")