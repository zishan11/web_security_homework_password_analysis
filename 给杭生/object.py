#coding:utf8
'''
此模块是为了生成三种键盘模式的密码
'''
import keyboardGet as kb
import random as rd
import pwdpartfunc as pf


keyboard = kb.GetKeyboardCor()
keychar = list(keyboard.keys())
keypos = list(keyboard.values())



def distance(charposi,charposj):
    '''
    计算两个字符的距离
    :param charposi: 第一个字符的坐标
    :param charposj: 第二个。。
    :return: 返回距离的平方
    '''
    return ((charposi[0]-charposj[0])**2+(charposi[1]-charposj[1])**2)
def getonepwd(limit,disoftype):
    '''
    生成一个密码，符合指定的模式，但是经过测试，zigzag类型的用这种方式消耗资源比较大，所以单独给他写了一个
    :param limit: 密码长度
    :param disoftype: 对应类型的距离
    :return: 返回一个密码
    '''
    pwd = ''
    # while len(pwd) < rd.randint(4,6):
    while len(pwd) < limit:
        indexchar = rd.randint(0,46)
        # print(keychar[indexchar])
        if pwd == '':
            if len(keychar) == 2:
                pwd += keychar[indexchar][rd.randint(0,1)]      #添加字符
            else:
                pwd += keychar[indexchar][0]
        else:
            chari = pf.toCharAray(pwd[-1])
            if len(keychar) == 2:
                charj = pf.toCharAray(keychar[indexchar][rd.randint(0,1)])
                if distance(chari, charj) == disoftype and charj[0]==chari[0]:
                    pwd += keychar[indexchar[rd.randint(0,1)]]

                # else:
                #     continue
            else:
                charj = pf.toCharAray(keychar[indexchar][0])
                if distance(chari, charj) == disoftype and charj[0]==chari[0]:
                    pwd += keychar[indexchar][0]
                # else:
                #     continue
    # while len(pwd)<limit:         #此段只是为了不使密码那么僵硬，增加了灵活度
    #     indexchar = rd.randint(0,46)
    #     flag = rd.randint(0,1)
    #     if flag == 0:
    #         pwd = pwd + keychar[indexchar][0]
    #     else:
    #         pwd = keychar[indexchar][0] +pwd
    return pwd

# print(getonepwd(8,5))
# a = pf.toCharAray('q')
# b = pf.toCharAray('s')
#
# print(distance(a,b))
# pwdgenerator = open('pwdjump.txt','w+')
#
# s = ''
# for i in range(10000):
#     pwd = getonepwd(rd.randint(6,10),4)
#     s = s + pwd + '\n'
#     # print(s)
# # print(s)
# pwdgenerator.write(s)
# pwdgenerator.close()

def getzigzag(limit,disoftype=2):
    '''
    单独生成zigzag的函数
    :param limit: 密码长度
    :param disoftype: 默认值为2
    :return: 返回密码
    '''
    pwd = ''
    while len(pwd) < limit:
        indexchar = rd.randint(0,46)
        # print(keychar[indexchar])
        if pwd == '':
            if len(keychar) == 2:
                pwd += keychar[indexchar][rd.randint(0,1)]      #添加字符
            else:
                pwd += keychar[indexchar][0]
        else:
            chari = pf.toCharAray(pwd[-1])
            if len(keychar) == 2:
                charj = pf.toCharAray(keychar[indexchar][rd.randint(0,1)])
                if (charj[0]==chari[0]+1 or charj[0]==chari[0]-1) and (chari[1]==charj[1]+1 or chari[1]==charj[1]-1):
                    if distance(chari, charj) == disoftype:
                        pwd += keychar[indexchar[rd.randint(0,1)]]

                # else:
                #     continue
            else:
                charj = pf.toCharAray(keychar[indexchar][0])
                if (charj[0]==chari[0]+1 or charj[0]==chari[0]-1) and (chari[1]==charj[1]+1 or chari[1]==charj[1]-1):
                    if distance(chari, charj) == disoftype:
                        pwd += keychar[indexchar][0]

    return pwd
# # print(keychar,'\n',keypos)
# # print(getzigzag(7))
# pwdgenerator = open('pwdzigzag.txt','w+')
#
# s = ''
# for i in range(10000):
#     pwd = getzigzag(rd.randint(6,10))
#     s = s + pwd + '\n'
#     # print(s)
# # print(s)
# pwdgenerator.write(s)
# pwdgenerator.close()
if __name__=='__main__':
    import object
    print(help(object))