#Lire un fichier texte dans une variable et remplacer toutes les nouvelles lignes par des espaces


def updateFile(file_name:str)->str:
    
    with open(file_name, 'r') as f:
        file = f.read()
        file = file.replace('\n',' ')
    
    #remplacer le contenu du fichier par le nouveau
    #with open(file_name, 'w') as f:
    #    f.write(file)
        
    return file


#Test
print(updateFile('file.txt'))
