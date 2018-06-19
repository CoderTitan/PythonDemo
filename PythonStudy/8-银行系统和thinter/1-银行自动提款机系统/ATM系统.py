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

from Admin import Admin

def main():
    # 欢迎页面
    admin = Admin()

    # 欢迎页面
    admin.printWelcomeView()
    if admin.adminOption():
        return -1


    while True:
        # 功能页面
        admin.printFunctionView()
        # 登陆成功, 等待用户操作
        option = input('请输入您的操作:')
        if option == '1':
            print('1')
        elif option == '2':
            print('2')
        elif option == '3':
            print('3')
        elif option == '4':
            print('4')
        elif option == '5':
            print('5')
        elif option == '6':
            print('6')
        elif option == '7':
            print('7')
        elif option == '8':
            print('8')
        elif option == '9':
            print('9')
        elif option == '0':
            print('0')
        elif option == 't':
            print('t')









if __name__ == '__main__':
    main()