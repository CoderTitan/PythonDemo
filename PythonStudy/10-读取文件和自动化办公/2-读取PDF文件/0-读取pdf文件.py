import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def readPDF(path, toPath):
    #以二进制形式打开pdf文件
    f = open(path, "rb")

    #创建一个pdf文档分析器
    parser = PDFParser(f)
    #创建pdf文档
    pdfFile = PDFDocument()
    #链接分析器与文档对象
    parser.set_document(pdfFile)
    # 保证双向链接
    pdfFile.set_parser(parser)
    #提供初始化密码
    pdfFile.initialize()

    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        # 结束
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据
        #数据管理器
        manager = PDFResourceManager()
        #创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manager, device)
        #开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            # 图层
            layout = device.get_result()
            for x in layout:
                # isinstance: 判断x的类型和LTTextBoxHorizontal是不是一样
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(toPath, "a") as f:
                        # 获取内容
                        str = x.get_text()
                        #print(str)
                        f.write(str+"\n")



path = r"/Users/quanjunt/Downloads/MongoDB1.pdf"
toPath = r"/Users/quanjunt/Documents/Quanjun/GitHub/PythonDemo/PythonStudy/10-读取文件和自动化办公/2-读取PDF文件/13.txt"
readPDF(path, toPath)
