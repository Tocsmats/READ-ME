fhand = open('maillog.txt')
counts = dict()

for line in fhand :
    line = line.rstrip()
    if line.startswith('From') :
        first = line.split()
        second = first[1]
        counts[second] = counts.get(second, 0) +1

lst = list()
for key, val in counts.items():
    fig = (val, key)
    lst.append(fig)
lst = sorted(lst, reverse=True)
for val, key in lst:
    print(key, val)
