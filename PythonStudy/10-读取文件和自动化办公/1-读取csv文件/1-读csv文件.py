

import csv


def readCsv(path):
    infoList = []
    with open(path, "r") as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)



        for row in allFileInfo:
            infoList.append(row)

    return infoList



path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/10-读取文件和自动化办公/1-读取csv文件/000001.csv"
info = readCsv(path)






