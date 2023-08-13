#Calculer la factorielle d’un nombre

def calculFactoriel(n:int)->int:
    
    if n < 0:
        return "Un nombre négatif n'a pas de factoriel"
    
    if n == 0:
        return 1
    else:
        return n * calculFactoriel(n-1)
    
    
    
#Test
print(calculFactoriel(6))