
import csv

def writeCsv(path, data):
    with open(path, 'w') as file:
        write = csv.writer(file)

        for rowData in data:
            print(rowData)

            write.writerow(rowData)



path = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/10-读取文件和自动化办公/1-读取csv文件/000003.csv"

writeCsv(path, [[1, 2, 3], [4, 6, 5], [0, 23, 45]])
