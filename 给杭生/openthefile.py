#coding:utf8
'''
模块1：openthefile.py（用作预处理，将老师给的文件处理为三个文件，分别保存密码，用户名即邮箱，密码+邮箱，这些作为中间文件为以后使用）
函数：只有一个OpenAndWrite(fname,allinfo,nameinfo,pwdinfo,seprator=‘:')
参数：fname是打开的文件名，allinfo为写入所有信息的文件，nameinfo只有名字，即邮箱，pwdinfo为密码文件，separator为分割符，默认为”:”
返回值：无

'''
__all__ = ['OpenAndWrite']
# import  re
import sys
# import codecs


def OpenAndWrite(fname,allinfo,nameinfo,pwdinfo,seprator=':'):          #fname是打开的文件名，allinfo为写入所有信息的文件，
    '''
    
    :param fname: 源数据文件
    :param allinfo: 将筛选的所有信息保存在此txt中
    :param nameinfo: 将邮箱保存到此txt中
    :param pwdinfo: 。。密码。。
    :param seprator: 分隔符，雅虎是'：'，CSDN是'#'
    :return: 无
    '''                                                                    # nameinfo只有名字，即邮箱，pwdinfo为密码文件，separator为分割符，默认为":"
    file = open(fname,'r',encoding = 'gbk',errors='ignore')
    listall = open(allinfo,'w')
    listname = open(nameinfo,'w')
    listpasswd = open(pwdinfo,'w')
    lines = file.readlines()
    if fname == 'plaintxt_yahoo.txt':       #判断是否是yahoo的，此处偷懒了
        lines = lines[3070:-1]              #把之前的无用东西省略
    # count = 0
    for line in lines:
        # line = line.encode('utf-8',errors='ignore').decode('utf-8',errors='ignore')
        line = line.encode('gbk',errors='ignore').decode('gbk',errors='ignore')
        line = line.split(seprator)
        count = 0
        email = ''
        passwd = ''
        emailandpasswd = ''
        for words in line:          #此处将邮箱、密码、整体分成三块，准备写入文件

            if count != 0:
                if count == 1:
                    email = words + '\n'
                    count += 1
                else:
                    passwd += ''.join(words)
                    count += 1
            else:
                count +=1
            emailandpasswd = '  '.join([email.replace('\n','    '),passwd])
            # passwd = line[2]
            # emailandpasswd = '   '.join(line[1:3])
        # email = email.encode('utf-8',errors='ignore').decode('utf-8',errors='ignore')
        # passwd = passwd.encode('utf-8',errors='ignore').decode('utf-8',errors='ignore')
        # emailandpasswd = emailandpasswd.encode('utf-8',errors='ignore').decode('utf-8',errors='ignore')
        listname.write(email)
        listpasswd.write(passwd)
        listall.write(emailandpasswd)
        # count += 1
        # if count <= 100:
        #     file2.write(line)
    file.close()
    listname.close()
    listpasswd.close()
    listall.close()

if __name__=='__main__':
    import openthefile
    print(help(openthefile))
    # fname = 'plaintxt_yahoo.txt'
    # allinfo = 'listall.txt'
    # nameinfo =  'listnames.txt'
    # pwdinfo = 'listpasswd.txt'
    # OpenAndWrite(fname,allinfo,nameinfo,pwdinfo)
