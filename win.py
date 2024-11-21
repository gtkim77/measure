import sys
from PyQt5.QtWidgets import QApplication, QWidget

class ExampleClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 500, 400)
        self.setWindowTitle('Empty Window in PyQT')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExampleClass()
    sys.exit(app.exec_())
