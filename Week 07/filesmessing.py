# lab work
# week 07
# author - Niall Wynne

FILENAME = 'count.txt'
def readnumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

num = readnumber()
print (num)