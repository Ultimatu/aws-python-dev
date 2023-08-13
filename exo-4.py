#Afficher un mot en alternant entre majuscules et minuscules

#Première méthode
def alternWord(word:str)->str:
    
    #parcourir le mot et mettre en majuscule les lettres d'index pair
    new_word = ''
    for i in range(len(word)):
        if i % 2 == 0: 
            new_word += word[i].upper()
        else:
            new_word += word[i].lower() 
    return new_word


#Deuxième méthode
def alternWord2(word:str)->str:
    
    #decouper en 2 2 2 et faire du capitalizing qui consiste à mettre la première lettre en majuscule
    new_word = ''
    for i in range(0,len(word),2):
        new_word += word[i:i+2].capitalize()
    return new_word


#Test
WORD = "Simplonisbest"

print(alternWord(WORD))
print(alternWord2(WORD))
