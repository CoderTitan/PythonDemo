from multiprocessing import Pool
import time, os


# 实现文件的拷贝
def copyFile(rPath, wPath):
    fr = open(rPath, 'rb')
    fw = open(wPath, 'wb')
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


path = ''
toPath = ''


# 不用进程操作
'''
# 读取path下的所有文件
fileList = os.listdir(path)

# for循环处理每一个文件
start = time.time()
for fileName in fileList:
    copyFile(os.path.join(path, fileName), os.path.join(toPath, fileName))

end = time.time()
print('总耗时: %.2f' % (end - start))
'''


# 多进程实现文件拷贝
if __name__ == '__main__':
    # 读取path下的所有文件
    fileList = os.listdir(path)

    # for循环处理每一个文件
    start = time.time()

    # 开启进程
    pool = Pool(4)
    for fileName in fileList:
        pool.apply_async(copyFile, args=(os.path.join(path, fileName), os.path.join(toPath, fileName)))

    pool.close()
    pool.join()

    end = time.time()
    print('总耗时: %.2f' % (end - start))












