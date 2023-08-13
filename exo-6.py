#Modifier l'élément d'une liste imbriquée
def updateNestedList(l:list, oldValue:int, newValue:int)->list:
    
    #parcourir la liste et remplacer les occurrences de oldValue par newValue et faire la même chose pour les listes imbriquées
    for i in range(len(l)):
        if type(l[i]) == list:
            updateNestedList(l[i], oldValue, newValue)
        elif l[i] == oldValue:
            l[i] = newValue
    return l


#Test
list1 = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]
oldvalue = 58
newvalue = 5800
print(updateNestedList(list1, oldvalue, newvalue))
