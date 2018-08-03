
import os





def reName(path):
    path1 = path + '/'
    nameList = os.listdir(path)

    for name in nameList:
        newName = 'ZXB' + name


        os.rename(path1 + name, path1 + newName)

        if os.path.isdir(path1 + newName):
            reName(path1 + newName)



path = r"/Users/quanjunt/Desktop/zcmlcSwift/ZXBUserInterface(用户界面)/ZXBReviewInterface(审核界面)"
reName(path)