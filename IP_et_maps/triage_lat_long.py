tab = []
a = 0
f = open("lats_trie.txt", "w")
data = open('long_lats.txt').readlines()

for i in range(len(data)):
    a += 1
    print(a)
    if data[i] in tab:
        continue
    else:
        tab.append(data[i])
        f.write(data[i])
        