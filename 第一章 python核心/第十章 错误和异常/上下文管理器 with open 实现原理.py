class openerTest(object):
    def open(self):
        print("文件被打开了")
    def operate(self,text_file):
        print("文件处理中！%s"%text_file)
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def close(self):
        print("文件被关闭了")

with openerTest() as f:
        f.operate("hhga.txt")
with open() as f:
    f.write()