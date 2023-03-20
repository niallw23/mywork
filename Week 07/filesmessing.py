# lab work
# week 07
# author - Niall Wynne

FILENAME = 'count.txt'
def readnumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number



def writenumber(number):
    with open(FILENAME, 'wt') as f:
        f.write(str(number))

num = readnumber()
num += 1
print (f'We have run this programme {num} times')
writenumber (num)