

# 导入son类
from Son import Son

def main():
    son = Son(200, 3000)
    print(son.money, son.faceValue)
    son.play()
    son.eat()

    # 父类中方法名相同, 默认调用的是在括号中排前面的父类中的方法
    son.run()



if __name__ == '__main__':
    main()






