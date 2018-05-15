#Tess Porter
#May 9, 2018
#CS 172-064

from Birthday import Birthday

f = open('bdaylist.txt', 'r')

h = []
for i in range(12):
    h.append([])

l = 1
for line in f:
    new_line = line.split('\n')
    b_day = new_line[0].split('/')
    b = Birthday(b_day[0], b_day[1], b_day[2])
    for count in range(12):
        if hash(b) == count:
            h[count].append((b, l))
    l += 1

count = 0
for list in h:
    print('Hash location', count, 'has', len(list), 'elements in it')
    count += 1

