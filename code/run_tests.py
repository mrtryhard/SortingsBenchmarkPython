#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time

# Auteur: Alexandre Leblanc. 

# Fichiers tests : 1 fichiers par algorithme. 
#                  1 paramètre entrant par fichier (liste des entiers)
#                  Chaque fichier doit être coder en python3.5
#tests_files = ["counting_sort.py", "heap_sort.py", "radix_sort.py", "quick_sort.py"]

import counting_sort
import heap_sort
import radix_sort
import quick_sort

# Tailles des tests.
tests_sizes = [10000, 20000, 40000, 80000, 160000, 320000, 640000, 1280000, 2560000, 5160000]

# Maximum de nombre de tests par taille par algorithme à faire. 
MAX_TESTS = 30 

# Crée la table de correspondances des temps courants
tests_time = [0 for _ in range(4)]

# Array de dictionnaires 
# [0: counting_sort]
# [i] => dict{size => time_sum}
dict_times_for_sizes = [dict() for _ in range(4)]

# Initialise les valeurs à 0 
for v in dict_times_for_sizes:
    for y in tests_sizes:
        v[y] = 0
        
        
# Crée la table de moyennes correspondante
tests_time_sum = [0 for _ in range(4)]

# On préchauffe la machine.
i = 0
while i < 1000000:
    i += 1

print("Début des tests, {0} tests par tailles:".format(MAX_TESTS))

for nb_elements_list_test in tests_sizes: 
    print("Tests {0} éléments...".format(nb_elements_list_test))
    
    i = 0
    while i < MAX_TESTS:
        # Génére une série de nombre aléatoire. 
        lst_input = [random.randint(1, 3000000) for _ in range (nb_elements_list_test)]
        max_elem = max(lst_input)
        
        # Clone d'objet, important! Pour éviter de biaiser les résultats.
        inp = lst_input[:]
        
        # Test counting_sort : 
        tests_time[0] = time.clock()
        counting_sort.tri_comptage(inp, max_elem)    
        tests_time[0] = time.clock() - tests_time[0]
        tests_time_sum[0] += tests_time[0]
        
        # Test heap_sort 
        # Clone d'objet, important! Pour éviter de biaiser les résultats.
        inp = lst_input[:]
        tests_time[1] = time.clock()
        heap_sort.tri_par_tas(inp)    
        tests_time[1] = time.clock() - tests_time[1]
        tests_time_sum[1] += tests_time[1]
        
        # Test radix sort 
        # Clone d'objet, important! Pour éviter de biaiser les résultats.
        inp = lst_input[:]
        tests_time[2] = time.clock()
        radix_sort.tri_par_base(inp)    
        tests_time[2] = time.clock() - tests_time[2]
        tests_time_sum[2] += tests_time[2] 
    
        # Test quick sort 
        tests_time[3] = time.clock()
        # Clone d'objet, important! Pour éviter de biaiser les résultats.
        inp = lst_input[:]
        quick_sort.tri_rapide(inp)    
        tests_time[3] = time.clock() - tests_time[3]
        tests_time_sum[3] += tests_time[3]         
        i += 1 
    
    # On sauvegarde les résultats (moyennes dans le dictionnaire)    
    dict_times_for_sizes[0][nb_elements_list_test] = (tests_time_sum[0] / MAX_TESTS)
    dict_times_for_sizes[1][nb_elements_list_test] = (tests_time_sum[1] / MAX_TESTS)
    dict_times_for_sizes[2][nb_elements_list_test] = (tests_time_sum[2] / MAX_TESTS)
    dict_times_for_sizes[3][nb_elements_list_test] = (tests_time_sum[3] / MAX_TESTS)
    
    print("\trésultats:")
    print("\t\tcounting_sort:\t{0}".format(dict_times_for_sizes[0][nb_elements_list_test]))
    print("\t\theap_sort:\t{0}".format(dict_times_for_sizes[1][nb_elements_list_test]))
    print("\t\tradix_sort:\t{0}".format(dict_times_for_sizes[2][nb_elements_list_test]))
    print("\t\tquick_sort:\t{0}".format(dict_times_for_sizes[3][nb_elements_list_test]))
    # next. 
        
# Overall, qui est meilleur ?
for test_size in tests_sizes:
    print("Pour un ensemble de taille {0}: ".format(test_size))
    print("\tcounting_sort:\t{0}".format(dict_times_for_sizes[0][test_size]))
    print("\theap_sort:\t{0}".format(dict_times_for_sizes[1][test_size]))
    print("\tradix_sort:\t{0}".format(dict_times_for_sizes[2][test_size]))
    print("\tquick_sort:\t{0}".format(dict_times_for_sizes[3][test_size]))
    print("\r\n")
