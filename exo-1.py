#Renverser une liste

#Première méthode : avec une fonction predéfinie reversed()
def reverse_list(l:list)->list:
    
    return list(reversed(l))



#Deuxième méthode : avec une boucle for
def reverse_list2(l:list)->list:
    
    new_list = []
    for i in range(len(l)):
        new_list.insert(0,l[i])
    return new_list



#Test 
test_list = [1,2,3,4,5,6,7,8,9,10]

print(reverse_list(test_list))

print(reverse_list2(test_list))















