'''
人
类名：User
属性：姓名  身份证号   电话号   卡
行为：


卡
类名：Card
属性：卡号   密码    余额
行为：



提款机
类名：ATM
属性：用户字典
行为：开户  查询   取款   存储   转账   改密    锁定     解锁   补卡   销户


管理员
类名：Admin
属性：
行为：管理员界面    管理员验证   系统功能界面


'''

import os
import time
import pickle  # 数据持久性模块
from Admin import Admin
from ATM import ATM

def main():
    # 欢迎页面
    admin = Admin()

    # 欢迎页面
    admin.printWelcomeView()
    if admin.adminOption():
        return -1


    # 提款机对象
    # 将当前的系统中的用户信息保存到文件中
    filePath = os.path.join(os.getcwd(), 'allusers.txt')
    file = open(filePath, 'rb')
    allUsers = pickle.load(file)
    print('******************************')
    print(allUsers)


    # ATM对象
    atm = ATM(allUsers)


    while True:
        # 功能页面
        admin.printFunctionView()

        # 登陆成功, 等待用户操作
        option = input('请输入您的操作:')
        if option == '1':
            atm.creatUser()
        elif option == '2':
            atm.searchUserInfo()
        elif option == '3':
            atm.getAccountMoney()
        elif option == '4':
            atm.saveMoney()
        elif option == '5':
            atm.transformAccountMoney()
        elif option == '6':
            atm.reviseAccountPassword()
        elif option == '7':
            atm.lockAccount()
        elif option == '8':
            atm.unlockAccount()
        elif option == '9':
            atm.reserAccountCard()
        elif option == '0':
            atm.removeAccount()
        elif option == 't':
            # 将当前系统中的用户信息保存到文件中
            file1 = open(filePath, 'wb')
            pickle.dump(atm.allUsers, file1)
            file1.close()

            time.sleep(2)
            print('退出成功')
            return -1




if __name__ == '__main__':
    main()