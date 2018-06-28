

import tkinter
import os

from infoWindows import InfoWindows
from treeWindows import TreeWindows

window = tkinter.Tk()

window.title('Titanjun')
window.geometry('800x400')


path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy"
infoWin = InfoWindows(window)
treeWin = TreeWindows(window, path, infoWin)



window.mainloop()







