import numpy as np

# On peut faire maintenant la meme chose avec le reste mais juste en 
# changeant le r, ex dates etc...
def dates():
    tab = []
    with open('controltower_access.log') as f:
        lignes = f.readlines()
        for line in lignes:
            r = line.split(' ')
            try:
                tab.append(r[13]) # Ajoute R au tablo
            except:
                pass
    return tab        

def spliter(tabo):
    tab = []
    with open('controltower_access.log') as f:
        lignes = f.readlines()
        longueur = len(lignes)

    for i in range(longueur):
        data = tabo[i].split(':') and tabo[i].split('/') # On separe la liste par rapport aux : et /
        data  = ([s.strip('[') for s in data])
        tab.append(data[0])
    return tab

def tablo(tabi):
    jours = open('os_trie.txt','w')
    for i in range(len(tabi)):
        jours.write(tabi[i])
        jours.write('\n')

tablo(dates())

# Je pense que ça marche pas car a chaque fois on appel dates dans 
# spliter,cta a chaque tour de boucle, la solution etait de tout