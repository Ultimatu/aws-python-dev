
#Afficher les nombres d’une liste qui sont divisibles par 5

#Première méthode
def displayDivisibleBy5(l:list)->list:
    
    #parcourir la liste et ajouter les nombres divisibles par 5 dans une nouvelle liste en plusieurs étapes
    new_list = []
    for i in range(len(l)):
        if l[i] % 5 == 0:
            new_list.append(l[i])
    return new_list

#================================================================================

#Deuxième méthode
def displayDivisibleBy5_2(l:list)->list:
    
    #parcourir la liste et ajouter les nombres divisibles par 5 dans une nouvelle liste en une seule étape
    return [l[i] for i in range(len(l)) if l[i] % 5 == 0]



#Test
test_list = [7, 5, 6, 45, 23, 40, 10, 18, 9, 77, 99, 100, 542, 1000, 1001, 1002, 1003, 1004, 1005]

print(displayDivisibleBy5(test_list))
print(displayDivisibleBy5_2(test_list))