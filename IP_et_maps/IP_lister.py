# Il sert tout simplement a lister les IP dans 'controltower_access et cree le fichier ip.txt

i = 0
f = open("ip.txt", "w")
for line in open('controltower_access.log'):
        ip = line.split(' ')[0]
        f.write(ip + '\n')
f.close()

# Ce programme sert pour creer un fichier avec toutes les ip dans 'controltower_access.log'
# En plus il print d'ou il vient chaque ip :)