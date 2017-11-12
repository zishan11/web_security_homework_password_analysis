#coding:utf8
'''
此文件为核心，判断一个密码是否为三种键盘模式之一
包括以下函数：
    toCharAray(s)   将单字符映射到键盘坐标
    CharToArray(Pwd)    将整个字母中所有的字符映射完的坐标保存在list中并返回
    Distance(PwdArray,i,j)  计算两个字符的距离的平方，i，j为两字符在PwdArray中的下标
    PanDuan(Pwd,limit,dis)    参数为密码、阈值（至少有多少个字符满足）
                                        、dis用来区分是哪种类型
                                        最后结果返回true或false
    SameRowClu(Pwd,limit)   同行判断                                 
    ZigZag(Pwd,limit)       斜线，w型之类的
    Jump(Pwd,limit)     跳棋式
'''
import sys

import keyboardGet as ky            #导入此文件，主要获取键盘的坐标

__all__ =['toCharAray','CharToArray','Distance','PanDuan','SameRowClu','ZigZag','Jump']
def  toCharAray(s):
    '''

    :param s: 要映射的单个字符
    :return: 返回此字符在键盘上的坐标
    '''
    # keyboard = {('`', '~'): (0, 0), ('1', '!'): (0, 1), ('2', '@'): (0, 2),
    #             ('3', '#'): (0, 3), ('4', '$'): (0, 4), ('5', '%'): (0, 5),
    #             ('6', '^'): (0, 6), ('7', '&'): (0, 7), ('8', '*'): (0, 8),
    #             ('9', '('): (0, 9), ('0', ')'): (0, 10), ('-', '_'): (0, 11),
    #             ('=', '+'): (0, 12), ('q',): (1, 1), ('w',): (1, 2), ('e',): (1, 3),
    #             ('r',): (1, 4), ('t',): (1, 5), ('y',): (1, 6), ('u',): (1, 7),
    #             ('i',): (1, 8), ('o',): (1, 9), ('p',): (1, 10), ('[', '{'): (1, 11),
    #             (']', '}'): (1, 12), ('\\', '|'): (1, 13), ('a',): (2, 1), ('s',): (2, 2),
    #             ('d',): (2, 3), ('f',): (2, 4), ('g',): (2, 5), ('h',): (2, 6),
    #             ('j',): (2, 7), ('k',): (2, 8), ('l',): (2, 9), (';', ':'): (2, 10),
    #             ('"', "'"): (2, 11), ('z',): (3, 1), ('x',): (3, 2), ('c',): (3, 3),
    #             ('v',): (3, 4), ('b',): (3, 5), ('n',): (3, 6), ('m',): (3, 7),
    #             (',', '<'): (3, 8), ('.', '>'): (3, 9), ('/', '?'): (3, 10)}
    keyboard = ky.GetKeyboardCor()
    s = s.lower().strip(' ')                                       # s has to be lower
    # flag = 0

    for keystu in keyboard.keys():
        if s in keystu:
            flag = 1
            return keyboard[keystu]
        # else:
    return (4,0)                #键盘坐标上没有此值，这般设置为了防止出错

def CharToArray(Pwd):                                   #protocol:Pwd is he password element
    '''

    :param Pwd: 输入的单个密码
    :return: 返回一个list，保存了每个字符对应的坐标
    '''
    PwdArray = []

    if Pwd != ''and Pwd != ' ':
        for s in Pwd:
            SingleArray = toCharAray(s)
            PwdArray.append(SingleArray)
        return PwdArray                                    #PwdArra是密码中每个字符按照键盘坐标转换之后的集合，并以list返回
    else:
        return []


def Distance(PwdArray,i,j):             #计算两个字符的距离的平方，主要为了方便，i，j为两字符在pwd中的下标
    '''

    :param PwdArray: 保存着密码中每个字符坐标的list
    :param i: 前一个字符在list中的下标
    :param j: 后一个字符的下标
    :return: 返回两个字符距离的平方
    '''
    return (PwdArray[i][0]-PwdArray[j][0])**2 + (PwdArray[i][1]-PwdArray[j][1])**2


# def PanDuan(Pwd,limit,dis,TypeOfPwd):                 #input Pwd ,limit of door ,distance of panduan, type of Pwd
def PanDuan(Pwd, limit, dis):
    '''

    :param Pwd:要判断的密码
    :param limit:连续判定的阈值，比如要求任意位置连续4个字符符合键盘模式，我才认定此密码为键盘模式，阈值limit此时设为4
    :param dis:距离，和键盘模式类型相关，同行或列为1，跳跃为4，斜列为2
    :return:返回True和False
    '''
    if len(Pwd) >= limit-1:
        begin = 0
        end = 0
        count = 0
        PwdArray = CharToArray(Pwd)
        for i in range(len(Pwd) - 1):
            count = end - begin + 1
            distance = Distance(PwdArray, i, i + 1)

            if count >= limit:
                # return [TypeOfPwd, Pwd]
                return True
            elif count < limit:
                distance = Distance(PwdArray, i, i + 1)
                if distance == dis:
                    # count += 1
                    end += 1
                else:
                    begin = end
                    end += 1
                    # return ['NonePattern',Pwd]
                    # return False
        if count >= limit:
            return True
        else:
            return False
        # count = end - begin
        # if count < limit:
        #     return ['NonePattern', Pwd]
    else:
        # return ['NonePattern',Pwd]
        return False

def SameRowClu(Pwd,limit):              #output a list ['type',Pwd]
    '''

    :param Pwd: 判别的密码
    :param limit: 阈值
    :return: 返回True或False
    '''
    # answer = PanDuan(Pwd,limit,1,'SameRowClu')
    answer = PanDuan(Pwd,limit,1)
    return answer

def ZigZag(Pwd,limit):
    '''

    :param Pwd: 密码
    :param limit: 阈值
    :return: True或False
    '''
    # answer = PanDuan(Pwd,limit,2,'ZigZag')
    answer = PanDuan(Pwd, limit, 2)
    return answer

def Jump(Pwd,limit):
    '''

    :param Pwd: 同上
    :param limit:
    :return:
    '''
    # answer = PanDuan(Pwd,limit,4,'Jump')
    answer = PanDuan(Pwd, limit, 4)
    return answer

if __name__=='__main__':
    import pwdpartfunc
    print(help(pwdpartfunc))
    print(SameRowClu('asdasdfg',4))
# print(ZigZag('clayton',5))
# print(Jump('ADGJLJ',4))

# s = input()
# print(toCharAray(s))