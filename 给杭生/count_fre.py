filesame = open('FreSameRowClu.txt','r')
filezigzag = open('FreZigZag.txt','r')
filejump = open('FreJump.txt','r')
def countword(file):
    countnum = 0
    Pwd = file.readline()
    while Pwd:
        Pwd = Pwd.strip('\n').split('   ')
        countnum += int(Pwd[1])
        # print(type(Pwd))
        Pwd = file.readline()
    return countnum
print(countword(filejump))
print(countword(filesame))
print(countword(filezigzag))