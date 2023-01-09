with open('controltower_access.log') as f:
    lines = f.readlines()
    for line in lines:
        r = line.split(' ')
        print(r[8]) # C'est la ou faut changer les r


# L'ordre des r :
# r[0] : Les ip
# r[1] / r[2] : rien
# r[3] : Heure et date
# r[4] : Zone de temps
# r[5] : Quelle requette HTTP (Get, Post, etc...)
# r[6] : Ce qui suit la requette HTTP
# r[7] : Pas interessant
# r[8] : Code reçue apres la requete (200, 404, etc...)
# r[9] : Pas interessant
# r[10] : Fichier donnee ( - si rien)
# r[11] : Navigateur
# r[12] : Kernel
# r[13] : OS
# r[14] : Pas interessant
# r[15] : Pas interessant, modele
# r[16] : Pas interessant
# r[17] : OUT OF RANGE !!!!