import matplotlib.pyplot as plt

def dico_jours():
    dico = {}
    with open('os_trie.txt') as f:
        lignes = f.readlines()
        for jours in lignes:
            if jours in dico:
                dico[jours] += 1
            else:
                dico[jours] = 1
    """Parcours le dictionnaire et si les valeurs sont egales a 1 on les supprime
    for cle, valeur in list(dico.items()):
        print(dico[valeur])
        if valeur == 1:
            del dico[cle]"""
    return dico

def graphique():
    plt.bar(dico_jours().keys(), dico_jours().values(), align='center', alpha=0.5)
    plt.xlabel('OS', labelpad=20)
    plt.xticks(rotation='vertical')
    plt.ylabel('Nombre de visites')
    plt.show()

# C'est reussi juste que le resultat final est que les tags dans le x axis sont beaucoup trop proches les uns des autres
# Mais ça marche ça c'est le plus important :)
graphique()