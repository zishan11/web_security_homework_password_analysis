#coding:utf8
'''
统计计数
一个函数：参数为一个输入文档，一个为输出文档
'''
import sys

file1 = 'listSameRowClu.txt'
file2 = 'listZigZag.txt'
file3 = 'listJump.txt'
filerow = 'FreSameRowClu.txt'
filezig = 'FreZigZag.txt'
filejump = 'FreJump.txt'

# from operator import *
def CountPwd(fname1,fname2):
    '''
    两个txt比对，有则计数加一，无则添加
    :param fname1: 源文件
    :param fname2: 频率文件
    :return: 无
    '''
    fileread = open(fname1,'r')
    filewrite = open(fname2,'w')
    lines = fileread.readlines()
    lst = {}
    for line in lines:
        # print(line)
        line = line.strip('\n').split('  ')
        # print(line)
        if line[1] in lst.keys():
            lst[line[1]] += 1
            # print(lst)
        else:
            lst[line[1]] = 1
    lst = dict(reversed(sorted(lst.items(),key=itemgetter(1))))
    # print(lst)
    for element in lst:
        # print(element)
        s = element + '   '+ str(lst[element])
        s += '\n'
        filewrite.write(s)
    fileread.close()
    filewrite.close()

if __name__ == '__main__':
    import CountFrequent
    print(help(CountFrequent))
    # CountPwd(file1,filerow)
    # CountPwd(file2,filezig)
    # CountPwd(file3,filejump)