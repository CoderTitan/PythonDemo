
from Users import Users
from Card import Card
import random

class ATM(object):
    def __init__(self, allUsers):
        # 所有用户
        self.allUsers = allUsers


    # 1.开户
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


    # 2.查询
    def searchUserInfo(self):
        cardNum = input('请输入您的卡号: ')
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)

        if self.checkAccountInfo(user):
            return -1

        print('账号: %s, 余额: %d' % (user.card.cardID, user.card.cardMoney))


    # 3.取款
    def getAccountMoney(self):
        cardNum = input('请输入您的卡号: ')
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)

        if self.checkAccountInfo(user):
            return -1
        print('账号: %s, 余额: %d' % (user.card.cardID, user.card.cardMoney))

        getMoney = int(input('请输入取款数额:'))
        if getMoney < 0:
            print('金额输入有误, 请重新操作!')
            return -1

        if getMoney > user.card.cardMoney:
            print('所取金额超过银行卡余额, 请重新操作')
            return -1

        user.card.cardMoney = user.card.cardMoney - getMoney
        print('取款成功, 余额: %d' % user.card.cardMoney)



    # 4.存款
    def saveMoney(self):
        cardNum = input('请输入您的卡号: ')
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)

        if self.checkAccountInfo(user):
            return -1
        print('账号: %s, 余额: %d' % (user.card.cardID, user.card.cardMoney))

        secondMoney = int(input('请输入存款数:'))
        if secondMoney < 0:
            print('金额输入有误, 请重新操作!')
            return -1

        user.card.cardMoney = secondMoney + user.card.cardMoney
        print('存款成功, 余额: %d' % user.card.cardMoney)


    # 5. 转账
    def transformAccountMoney(self):
        pass


    # 6.改密码
    def reviseAccountPassword(self):
        cardNum = input('请输入您的卡号: ')
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)

        if self.checkAccountInfo(user):
            return -1

        newPass = input('请输入新密码:')
        if not self.checkPassword(newPass):
            print('密码输入错误, 操作失败!')
            return -1
        user.card.passwd = newPass


    # 7.锁定账户
    def lockAccount(self):
        cardNum = input('请输入您的卡号: ')
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)

        if self.checkAccountInfo(user):
            return -1

        tempIDCard = input('请输入身份证号码:')
        if not tempIDCard == user.idCard:
            print('身份证信息有误, 锁定失败')
            return -1

        user.card.cardLock = True
        print('锁定成功')


    # 8.解锁
    def unlockAccount(self):
        cardNum = input('请输入您的卡号: ')
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)

        if self.checkAccountInfo(user):
            return -1

        # 身份信息
        tempIDCard = input('请输入身份证号码:')
        if not tempIDCard == user.idCard:
            print('身份证信息有误, 锁定失败')
            return -1

        user.card.cardLock = False
        print('解锁成功')


    # 9.补卡
    def reserAccountCard(self):
        cardNum = input('请输入您的卡号: ')
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)

        if self.checkAccountInfo(user):
            return -1

        # 身份信息
        tempIDCard = input('请输入身份证号码:')
        if not tempIDCard == user.idCard:
            print('身份证信息有误, 锁定失败')
            return -1

        user.card.cardID = self.getRandomCardID()


    # 0.销户
    def removeAccount(self):
        cardNum = input('请输入您的卡号: ')
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)

        if self.checkAccountInfo(user):
            return -1

        # 身份信息
        tempIDCard = input('请输入身份证号码:')
        if not tempIDCard == user.idCard:
            print('身份证信息有误, 锁定失败')
            return -1

        del self.allUsers[cardNum]
        print(self.allUsers)


    # 检测卡号是否存在, 是否锁定, 验证密码
    def checkAccountInfo(self, user):
        if not user:
            print('该卡不存在, 请重新输入.')
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print('该卡已锁定, 请先解锁再重新操作')
            return -1

        # 验证密码
        if not self.checkPassword(user.card.passwd):
            print("密码错误, ")
            user.card.cardLock = True
            return -1


    # 检测两次输入的密码是否一致
    def checkPassword(self, realPasswd):
        for i in range(3):
            tempPass = input('请输入密码:')
            if tempPass == realPasswd:
                return True

        print('密码错误, 请重新输入')
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