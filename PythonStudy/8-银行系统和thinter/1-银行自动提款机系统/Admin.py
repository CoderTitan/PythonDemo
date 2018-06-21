
# 管理员类

import time

class Admin(object):
    # 账户
    admin = "t"
    # 密码
    passwd = 't'

    # 欢迎页面
    def printWelcomeView(self):
        print("*******************************************************************")
        print("**                                                               **")
        print("**                                                               **")
        print("**                       欢迎登陆TitanJun银行                      **")
        print("**                                                               **")
        print("**                                                               **")
        print("*******************************************************************")

    # 功能页面
    def printFunctionView(self):
        print("*****************************************************************")
        print("*        开户(1)                            查询(2)               *")
        print("*        取款(3)                            存款(4)               *")
        print("*        转账(5)                            改密(6)               *")
        print("*        锁定(7)                            解锁(8)               *")
        print("*        补卡(9)                            销户(0)               *")
        print("*                          退出(t)                               *")
        print("*****************************************************************")

    # 输入账号密码
    def adminOption(self):
        inputAdmin = input('请输入管理员账号: ')
        if self.admin != inputAdmin:
            print('账号输入有误, 请重新输入')
            return -1

        inputPasswd = input('请输入管理员密码: ')
        if self.passwd != inputPasswd:
            print('密码输入有误, 请重新输入')
            return -1

        # 账号密码正确
        print('登录成功, 请稍后...')
        time.sleep(2)
        return 0







