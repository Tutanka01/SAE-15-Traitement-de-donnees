# Ce programme il sert juste a trier les IP dans le fichier ip.txt

data = open('ip.txt').readlines()
f = open("ip_trie.txt", "w")
tablo_ip = []


for i in range(len(data)):
    if data[i] in tablo_ip:
        continue
    else:
        tablo_ip.append(data[i])
        f.write(data[i])
    
    
    # Sinon il va ecrire dans le nouveau fichier
    # Il cree un nouveau fichier ou il tri les addresses ip pour passer
    # de 268351 ip a 150000, leger imporvemment
