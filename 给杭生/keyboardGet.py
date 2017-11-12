#coding:utf8

'''

此代码主要为了将键盘映射成二维数组，以及各符号和字母的坐标，以元组为元素保存在dict中

'''
__all__ = ['GetKeyboardCor()']

import sys

def GetKeyboardCor():
    '''

    :return: 调用即返回键盘上可视字符对应的坐标，返回字典类型
    '''
    file = open('keyboard.txt','r')
    lines = file.readlines()
    keyboard ={}

    for i in range(47):
        s = tuple(lines[i].strip('\n').split(' '))
        state = []
        if i <= 25:
            if i <=12:
                state = [0,i]
                statevalue = tuple(state)
                keyboard[s] = statevalue
            else:
                state = [1,i-12]
                statevalue = tuple(state)
                keyboard[s] = statevalue
        elif i <= 46:
            if i <= 36:
                state = [2,i-25]
                statevalue = tuple(state)
                keyboard[s] = statevalue
            else:
                state = [3, i - 36]
                statevalue = tuple(state)
                keyboard[s] = statevalue
    return keyboard

if __name__ =='__main__':
    import keyboardGet
    print(help(keyboardGet))
    # print(len(GetKeyboardCor()))
