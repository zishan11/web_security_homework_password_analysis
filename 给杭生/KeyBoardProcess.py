#coding:utf8

'''
此文件是为了处理指定的密码文件，将其按三种键盘模式分开，输出到三个指定的txt文档中

'''
import sys
import keyboardGet
import openthefile
from pwdpartfunc import *


def writeinfile(s,fname):
    '''
    将字符串写入文件
    :param s: 字符串
    :param fname: 文件名
    :return: 无
    '''
    with open(fname,'w') as f:
        # for words in s:
        f.write(s)


# def KeyBoardModel(pwdFile,samerowFile,zigzagFile,jumpFile):

def KeyBoardModel():
    '''

    :return: 将符合三种模式的密码识别出来并且放入到三个txt中
    '''
    pwdFile = 'listpasswd.txt'
    # samerowFile = 'listest.txt'
    # File = open(pwdFile,'r',encoding='gbk',errors='ignore')
    File = open(pwdFile, 'r')
    # FileSameRowClu = open(samerowFile,'w')
        # FileZigZag = open(zigzagFile,'w')
        # FileJump = open(jumpFile,'w')

    # File = open('listpasswd.txt', 'r', encoding='gbk', errors='ignore')
    FileSameRowClu = open('listSameRowClu.txt', 'w')
    FileZigZag = open('data/listZigZag.txt', 'w')
    FileJump = open('data/listJump.txt', 'w')
    list_same_row = []
    list_zigzag = []
    list_jump = []
    # PwdAll = File.readlines()
    # count = 0
    # s = []
    # for Pwd in PwdAll:
    Pwd = File.readline()
    while Pwd:
        # Pwd = Pwd.encode('gbk',errors='ignore').decode('gbk',errors='ignore')

        # print(Pwd)
        Pwd = Pwd.strip('\n')
        # print(Pwd)

        # if count == 10:
        #     break
        # else:
        #     s.append(Pwd)
        #     print(s)
        # count += 1

        # result1 = SameRowClu(Pwd,4)
        # # print(result1)
        # result2 = ZigZag(Pwd,4)
        # # print(result2)
        # result3 = Jump(Pwd,4)
        # if SameRowClu(Pwd,4) != None and SameRowClu(Pwd,4)[0] == 'SameRowClu':
        if SameRowClu(Pwd, 4):
            # s = '   '.join(SameRowClu(Pwd,4))
            s = 'SameRowClu'+'  '+Pwd
            s += '\n'
            # list_same_row.append(s)
            # print('samerow',s)
            FileSameRowClu.write(s)
            Pwd = File.readline()
            continue
        Pwd = File.readline()
        # print(Pwd)
        # # ZigZag(Pwd,4)[0] == 'ZigZag':
        # # if ZigZag(Pwd,4) != None and ZigZag(Pwd,4)[0] == 'ZigZag':
        # if ZigZag(Pwd, 4) != None and ZigZag(Pwd, 4):
        if ZigZag(Pwd, 4):
            # s = '   '.join(ZigZag(Pwd,4))
            s = 'ZigZag'+'  '+Pwd
            s += '\n'
            # print('zigzag',s)
            # list_zigzag.append(s)
            print(s)
            FileZigZag.write(s)
            Pwd = File.readline()
            continue
        Pwd = File.readline()
        # # if Jump(Pwd,4) != None and Jump(Pwd,4)[0] == 'Jump':
        # if Jump(Pwd, 4) != None and Jump(Pwd, 4):
        if Jump(Pwd, 4):
            # s = '   '.join(Jump(Pwd,4))
            s = 'Jump'+'    '+Pwd
            s += '\n'
            # print('jump',s)
            # list_jump.append(s)
            FileJump.write(s)
            Pwd = File.readline()
            continue
        Pwd = File.readline()
    # list_same_row = '   '.join(list_same_row)
    # list_zigzag = '   '.join(list_zigzag)
    # list_jump = '   '.join(list_jump)
    # writeinfile(list_same_row,samerowFile)
    # writeinfile(list_zigzag,zigzagFile)
    # writeinfile(list_jump,jumpFile)
    print('process end!')
    File.close()
    FileSameRowClu.close()
    FileZigZag.close()
    FileJump.close()

if __name__=='__main__':
    import KeyBoardProcess
    print(help(KeyBoardProcess))
#     specificFile = 'listpasswd.txt'
#     specificFileSameRowClu = 'data/listSameRowClu.txt'
#     specificFileZigZag = 'data/listZigZag.txt'
#     specificFileJump = 'data/listJump.txt'
#     KeyBoardModel(specificFile,specificFileSameRowClu,specificFileZigZag,specificFileJump)