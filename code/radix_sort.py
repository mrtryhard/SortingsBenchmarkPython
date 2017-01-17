#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math 

# Tri par base (RadixSort)
# lst : liste à trier 
# max_len : longueur max d'un nombre (int: 10)
def tri_par_base(lst, max_len = 10):
    # un nombre n'aura pas plus que 10 digit.
    NB_BUCKETS = 10 
    for x in range(max_len):
        # Initialise les buckets 
        buckets = [[] for i in range(NB_BUCKETS)]
        
        # Pour chaque élément dans la liste on l'affecte à son bucket. 
        for y in lst:
            buckets[math.floor( (y / 10 ** x) % NB_BUCKETS)].append(y)
        
        # Applati le bucket. 
        lst = []
        for section in buckets:
            lst.extend(section)
            
    return lst

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Requires list.")
    else:
        list_of_integers = [int(i) for i in sys.argv[1:]]
     
        lst = tri_par_base(list_of_integers)
    
        print("Sorted List: ")
        print(lst)
        print("Radix sort end.")