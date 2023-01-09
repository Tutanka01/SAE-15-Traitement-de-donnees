import matplotlib.pyplot as plt

def dico_jours():
    dico = {}
    with open('navig_trie.txt') as f:
        lignes = f.readlines()
        for jours in lignes:
            if jours in dico:
                dico[jours] += 1
            else:
                dico[jours] = 1
    return dico
def graphique():
    plt.bar(dico_jours().keys(), dico_jours().values())
    plt.xlabel('Navig', labelpad=20)
    plt.xticks(rotation='vertical')
    plt.ylabel('Nombre')
    plt.show()

# C'est reussi juste que le resultat final est que les tags dans le x axis sont beaucoup trop proches les uns des autres
# Mais ça marche ça c'est le plus important :)
graphique()