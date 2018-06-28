
from tkinter import *
from tkinter import ttk
import os

class TreeWindows(Frame):
    def __init__(self, master, path, otherWin):
        frame = Frame(master)
        frame.grid(row=0, column=0)

        self.otherWin = otherWin

        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=LEFT, fill=Y)

        # print(os.path.splitext(path))

        tempPath = self.getLastPath(path)
        root = self.tree.insert('', 'end', text=tempPath, open=True, values=(path))
        self.loadTree(root, path)

        # 滚动条
        self.sv = Scrollbar(frame)
        self.sv.pack(side=RIGHT, fill=Y)
        self.sv.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sv.set)

        # 绑定事件
        self.tree.bind('<<TreeviewSelect>>', self.treeSelected)


    def treeSelected(self, event):
        self.v = event.widget.selection()

        for sv in self.v:
            file = self.tree.item(sv)['text']
            self.otherWin.ev.set(file)
            apath = self.tree.item(sv)['values']
            print(apath)



    def loadTree(self, parent, parentPath):
        # listdir: 返回指定文件下的所有文件
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath, fileName)

            # 插入树枝
            treey = self.tree.insert(parent, 'end', text=self.getLastPath(absPath), values=(absPath))
            # 判断是否是目录
            if os.path.isdir(absPath):
                self.loadTree(treey, absPath)




    def getLastPath(self, path):
        pathLast = os.path.split(path)
        return pathLast[-1]