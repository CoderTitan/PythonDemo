
from Users import Users
from Card import Card
import random

class ATM(object):
    def __init__(self, allUsers):
        # 所有用户
        self.allUsers = allUsers


    # 开户
    def creatUser(self):
        name = input('请输入姓名:')
        idCard = input('请输入身份证号:')
        phoneNum = input('请输入手机号:')
        money = int(input('请输入存款金额:'))

        if money < 0:
            print('金额输入有误, 请重新操作!')
            return -1

        passwd = input('请输入密码:')
        # 检测密码是否符合规则
        if not self.checkPassword(passwd):
            print('密码输入错误, 操作失败!')
            return -1

        # 到这里说明所有信息就都正确了
        cardStr = self.getRandomCardID()
        card = Card(cardStr, passwd, money)
        user = Users(name, idCard, phoneNum, card)

        # 存到字典中
        self.allUsers[cardStr] = user
        print('开户成功, 请牢记卡号: (%s)' % cardStr)


    # 查询


    # 取款




    # 检测两次输入的密码是否一致
    def checkPassword(self, realPasswd):
        for i in range(3):
            tempPass = input('请输入密码:')
            if tempPass == realPasswd:
                return True

        return False

    # 获取银行卡号(随机)
    def getRandomCardID(self):
        while True:
            str = ''
            for i in range(10):
                # ord(x): 将一个字符转换为它的整数值
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch

            # 判断是否重复
            if not self.allUsers.get(str):
                return str