import folium
carte = folium.Map(location=[43.640512, 5.102072],zoom_start = 0)
# Long_Lats ne doit pas avoir ni parentheses ni virgules

for line in open('tricord.txt'):  # Ouvre le fichier
    line = line.strip('\n')         # Enleve le saut a la ligne
    coord = line.split(' ') # Enleve l'espace ??
    folium.Marker(location = coord, tooltip="Ce point est le num :{}".format(coord)).add_to(carte) # Rajoute dans la carte GPS le points avec les coordonnees

carte.save('Carte.html')

