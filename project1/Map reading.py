f= open('locations.txt', 'r')
dict1 = {}
line1 =f.readlines()
c = None
for i in range(len(line1)):
    if 'LOCATION' in line1[i]:
        c = line1[i].strip()
        list1 = [line1[i + 1]]
        dict1[c] = list1
    else:
        list2=[line1[i]]
        dict1[c] += list2
print(dict1)
