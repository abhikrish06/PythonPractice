file = open('/home/krishna/Desktop/links.txt', 'r')
dct = {}
for line in file:
    print(line)
    if len(line) > 0 and '- -' in line:
        sp = line.split('- -')
        if sp[0] in dct:
            dct[sp[0]] += 1
        else:
            dct[sp[0]] = 1

print(dct)

file.close()

file2 = open('/home/krishna/Desktop/output.txt', 'w')

for k,v in dct.items():
    l = k+' '+str(v)
    file2.write(l)
    file2.write('\n')

file2.close()

