# 使用wxPython或PyQt5创建一个窗口，实现可以实现浏览、选择本地文本文件，且可以编辑文件内容
# 文件编码
# 同时编辑多个文件
# Author: TangYue

from PyQt5.QtWidgets import QFileDialog, QApplication, QTextEdit, QWidget, \
    QPushButton
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QIcon
import sys


class Ui_test:
    def __init__(self):
        self.creat_info()
        self.printer = QPrinter()

    def creat_info(self):
        self.w = QWidget()
        self.w.setGeometry(400, 400, 500, 500)
        self.w.setWindowTitle('文本编辑by tang')
        self.w.setWindowIcon(QIcon('wx.jpg'))
        self.creat_res()
        self.w.show()

    def creat_res(self):
        self.t1 = QTextEdit(self.w)
        self.t1.setGeometry(15, 15, 300, 400)
        self.B_openfile = QPushButton('打开文件', self.w)
        self.B_openfile.setGeometry(350, 15, 100, 30)
        self.B_openmorefile = QPushButton('打开多文件', self.w)
        self.B_openmorefile.setGeometry(350, 65, 100, 30)
        self.save_file = QPushButton('保存文件', self.w)
        self.save_file.setGeometry(350, 115, 100, 30)
        self.clear_file = QPushButton('清除文本', self.w)
        self.clear_file.setGeometry(350, 165, 100, 30)
        self.config()

    def config(self):
        self.B_openfile.clicked.connect(self.open_file)
        self.B_openmorefile.clicked.connect(self.open_files)
        self.clear_file.clicked.connect(self.clear_all)
        self.save_file.clicked.connect(self.save_files)

    def clear_all(self):
        self.t1.clear()

    def open_file(self):
        files = QFileDialog.getOpenFileName(self.w, '打开本地文件')
        if files[0]:
            with open(files[0], mode='r', encoding='gb18030',
                      errors='ignore') as f:
                self.t1.setText(f.read())

    def open_files(self):  # 此处获取得是多个文件，返回得是文件列表
        files = QFileDialog.getOpenFileNames(self.w, '打开本地文件')
        print(files)
        if files[0]:
            for file in files[0]:
                with open(file, mode='r', encoding='gb18030',
                          errors='ignore') as f:
                    self.t1.append(f.read())

    def save_files(self):
        file = QFileDialog.getSaveFileName(self.w, '保存文件')
        if file[0]:
            with open(file[0], mode='r', encoding='gb18030',
                      errors='ignore') as f:
                f.write(self.t1.toPlainText())


ap = QApplication(sys.argv)
u = Ui_test()
sys.exit(ap.exec_())
