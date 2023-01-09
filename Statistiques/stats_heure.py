tab = []
with open('controltest.log') as f:
    lines = f.readlines()
    for line in lines:
        r = line.split(' ')# C'est la ou faut changer les r
        a = r[3].replace('[', '')
        tab.append(a)

print(tab)
