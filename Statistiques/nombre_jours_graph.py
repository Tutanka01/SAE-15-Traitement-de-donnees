import matplotlib.pyplot as plt

def dico_jours():
    dico = {}
    with open('jours_trie.txt') as f:
        lignes = f.readlines()
        for jours in lignes:
            if jours in dico:
                dico[jours] += 1
            else:
                dico[jours] = 1
    return dico

def graphique():
    plt.bar(dico_jours().keys(), dico_jours().values())
    plt.show()
    
graphique()

