# web_security_homework_password_analysis
web安全大作业，密码模式分析，生成，强度分析
NAME
    openthefile

DESCRIPTION
    模块1：openthefile.py（用作预处理，将老师给的文件处理为三个文件，分别保存密码，用户名即邮箱，密码+邮箱，这些作为中间文件为以后使用）
    函数：只有一个OpenAndWrite(fname,allinfo,nameinfo,pwdinfo,seprator=‘:')
    参数：fname是打开的文件名，allinfo为写入所有信息的文件，nameinfo只有名字，即邮箱，pwdinfo为密码文件，separator为分割符，默认为”:”
    返回值：无

FUNCTIONS
    OpenAndWrite(fname, allinfo, nameinfo, pwdinfo, seprator=':')
        :param fname: 源数据文件
        :param allinfo: 将筛选的所有信息保存在此txt中
        :param nameinfo: 将邮箱保存到此txt中
        :param pwdinfo: 。。密码。。
        :param seprator: 分隔符，雅虎是'：'，CSDN是'#'
        :return: 无

DATA
    __all__ = ['OpenAndWrite']

FILE
    /Users/luanshijie/研究生课程学习内容/web安全/给杭生/openthefile.py


NAME
    keyboardGet - 此代码主要为了将键盘映射成二维数组，以及各符号和字母的坐标，以元组为元素保存在dict中

DATA
    __all__ = ['GetKeyboardCor()']

FILE
    /Users/luanshijie/研究生课程学习内容/web安全/给杭生/keyboardGet.py


NAME
    pwdpartfunc

DESCRIPTION
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

FUNCTIONS
    CharToArray(Pwd)
        :param Pwd: 输入的单个密码
        :return: 返回一个list，保存了每个字符对应的坐标

    Distance(PwdArray, i, j)
        :param PwdArray: 保存着密码中每个字符坐标的list
        :param i: 前一个字符在list中的下标
        :param j: 后一个字符的下标
        :return: 返回两个字符距离的平方

    Jump(Pwd, limit)
        :param Pwd: 同上
        :param limit:
        :return:

    PanDuan(Pwd, limit, dis)
        :param Pwd:要判断的密码
        :param limit:连续判定的阈值，比如要求任意位置连续4个字符符合键盘模式，我才认定此密码为键盘模式，阈值limit此时设为4
        :param dis:距离，和键盘模式类型相关，同行或列为1，跳跃为4，斜列为2
        :return:返回True和False

    SameRowClu(Pwd, limit)
        :param Pwd: 判别的密码
        :param limit: 阈值
        :return: 返回True或False

    ZigZag(Pwd, limit)
        :param Pwd: 密码
        :param limit: 阈值
        :return: True或False

    toCharAray(s)
        :param s: 要映射的单个字符
        :return: 返回此字符在键盘上的坐标

DATA
    __all__ = ['toCharAray', 'CharToArray', 'Distance', 'PanDuan', 'SameRo...

FILE
    /Users/luanshijie/研究生课程学习内容/web安全/给杭生/pwdpartfunc.py


NAME
    KeyBoardProcess - 此文件是为了处理指定的密码文件，将其按三种键盘模式分开，输出到三个指定的txt文档中

FUNCTIONS
    KeyBoardModel()
        :return: 将符合三种模式的密码识别出来并且放入到三个txt中

    writeinfile(s, fname)
        将字符串写入文件
        :param s: 字符串
        :param fname: 文件名
        :return: 无

FILE
    /Users/luanshijie/研究生课程学习内容/web安全/给杭生/KeyBoardProcess.py

NAME
    CountFrequent

DESCRIPTION
    统计计数
    一个函数：参数为一个输入文档，一个为输出文档

FUNCTIONS
    CountPwd(fname1, fname2)
        两个txt比对，有则计数加一，无则添加
        :param fname1: 源文件
        :param fname2: 频率文件
        :return: 无

DATA
    file1 = 'listSameRowClu.txt'
    file2 = 'listZigZag.txt'
    file3 = 'listJump.txt'
    filejump = 'FreJump.txt'
    filerow = 'FreSameRowClu.txt'
    filezig = 'FreZigZag.txt'

FILE
    /Users/luanshijie/研究生课程学习内容/web安全/给杭生/CountFrequent.py

NAME
    object - 此模块是为了生成三种键盘模式的密码

FUNCTIONS
    distance(charposi, charposj)
        计算两个字符的距离
        :param charposi: 第一个字符的坐标
        :param charposj: 第二个。。
        :return: 返回距离的平方

    getonepwd(limit, disoftype)
        生成一个密码，符合指定的模式，但是经过测试，zigzag类型的用这种方式消耗资源比较大，所以单独给他写了一个
        :param limit: 密码长度
        :param disoftype: 对应类型的距离
        :return: 返回一个密码

    getzigzag(limit, disoftype=2)
        单独生成zigzag的函数
        :param limit: 密码长度
        :param disoftype: 默认值为2
        :return: 返回密码

DATA
    __warningregistry__ = {'version': 0, ("unclosed file <_io.TextIOWrappe...
    keyboard = {('"', "'"): (2, 11), (',', '<'): (3, 8), ('-', '_'): (0, 1...
    keychar = [('`', '~'), ('1', '!'), ('2', '@'), ('3', '#'), ('4', '$'),...
    keypos = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, ...

FILE
    /Users/luanshijie/研究生课程学习内容/web安全/给杭生/object.py
