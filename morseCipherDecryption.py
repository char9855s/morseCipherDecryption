def Offset(offset):  # 密码偏移函数
    global password  # 声明password，向上级寻找password
    new_password = ''  # 创建一个新的变量用于存放偏移后的字母
    for i in password:
        if 97 <= ord(i) <= 122:
            # print(ord(i),type(offset),offset)
            if ord(i) + int(offset) > 122:  # 对超范围的值重新回到范围
                new_password += chr(ord(i) + int(offset) - 26)
            elif ord(i) + int(offset) < 97:
                new_password += chr(ord(i) + int(offset) + 26)
            else:
                new_password += chr(ord(i) + int(offset))
        else:
            new_password += i  # 对非字母部分进行保留
    return new_password  # 将new_password作为结果返回


def Number(offset):
    try:
        a = int(offset)
        return True
    except:
        return False


a_list = []  # 储存用户输入内容
password = ''
a_dict = {
    '.-': 'a', '..': 'i', '--.-': 'q', '-.--': 'y', '-----': '0', '..---': '2', '....-': '4',
    '-...': 'b', '.---': 'j', '.-.': 'r', '--..': 'z', '.----': '1', '...--': '3', '.....': '5',
    '-.-.': 'c', '-.-': 'k', '...': 's', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-..': 'd', '.-..': 'l', '-': 't',
    '.': 'e', '--': 'm', '..-': 'u',
    '..-.': 'f', '-.': 'n', '...-': 'v',
    '--.': 'g', '---': 'o', '.--': 'w',
    '....': 'h', '.--.': 'p', '-..-': 'x'
}  # 储存密码表
a_list2 = [',', '，', '。', '.']  # 存储符号
str1 = ''  # 获取每个输入内容
if __name__ == '__main__':
    a_list = input("请输入摩斯密码:(空格为每组摩斯密码的间隔)").split(' ')
    for str1 in a_list:  # str 遍历每组内容
        # if str1 == ' ':
        #     password = password + ' '
        #     continue
        n = a_dict.get(str1, False)  # 如果输入内容合法，在密码表中寻找，找到则返回结果，未找到则返回False
        if n:
            password = password + n  # 记录每个字母
            # print(n)
            n = ''  # 对n值进行清空
        else:
            if str1 in a_list2:
                password += str1
            elif str1 is None:
                password += ' '
            else:
                password = password + ' ' + str1 + ' '
    print(password)  # 输出结果
    # 密码偏移
    while True:
        offset = input("请输入偏移值，没有偏移值输入零，向左偏移为负数：")
        if Number(offset):  # 判断输入是否为纯数字
            # 是纯数字
            offset = int(offset)  # 将输入内容转化为整型
            password = Offset(offset)  # 进行字母偏移
            print(password)  # 打印结果
            break  # 函数结束
        else:  # 不是纯数字
            print("输入异常，请重新输入")