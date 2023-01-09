import time
from get_ip import *
i = 0
f = open("lats_longs.txt", "w")
a = True

def sleep_minutes(min):
        min = min * 60
        time.sleep(min)

try:
        for line in open('ip.txt'):
                line = line.strip('\n')                 # Il va enlever le \n
                ip_loc = get_loc(line)                  # Trouver la lattitude et longitude d'une IP
                print(ip_loc)
                f.write(str(ip_loc) + '\n')
                sleep_minutes(4)
        f.close()
except:
        pass

# Ce programme sert pour creer un fichier avec toutes les ip dans 'controltower_access.log'
# En plus il print d'ou il vient chaque ip :)