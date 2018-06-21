# 主窗口
import tkinter

# 验证输入的文字
def varileText():
    text = entry4.get()
    if text != '1':
        print('对喽')
        return True
    print('错漏')
    return False

#
def testInvaild():
    print('invaildCommanf被调用')
    return True


# 创建主窗口
window = tkinter.Tk()

# 设置标题
window.title('Titanjun')

# 设置窗口大小
window.geometry('400x400')



button = tkinter.Button(window, text='Titan', bg='#ff4040')
button.pack()



'''
输入控件
用于显示简单的文本内容
'''

vari = tkinter.Variable()
entry = tkinter.Entry(window, textvariable=vari)
entry.pack()

# 设置值
vari.set('very good')
# 取值
print(vari.get())
print(entry.get())

# 只读输入框
vari2 = tkinter.Variable()
entry2 = tkinter.Entry(window, textvariable=vari2, state='disabled')
entry2.pack()

# 设置值
vari2.set('very bad')
print(vari2.get())

# 密码输入框, 无论输入什么都显示密文
vari3 = tkinter.Variable()
entry3 = tkinter.Entry(window, textvariable=vari3, show='@', bg='red', fg='white')
entry3.pack()


# 验证输入的内容是否符合要求
vari4 = tkinter.Variable()
entry4 = tkinter.Entry(window, textvariable=vari4, validate='key', validatecommand=varileText, invalidcommand=testInvaild)
entry4.pack()



# 进入消息循环
window.mainloop()



