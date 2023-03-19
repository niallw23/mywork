# messing with files
# mirroring lecture work

FILENAME = 'data.txt'

with open (FILENAME, 'r') as f:
    data = f.read()
    print(data)

with open ('data2.txt', 'wt') as f:
    f.write ('His name is Chase\n')
    f.write ('Not Chester')