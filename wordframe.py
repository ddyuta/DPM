count = 0
with open('city011/city011_001.txt') as f:
    for line in f:
        count += 1
        if count == 2:
            name = line.strip()
framenum = count -3
print('number of frame')
print (name + ' : ' + str(framenum))