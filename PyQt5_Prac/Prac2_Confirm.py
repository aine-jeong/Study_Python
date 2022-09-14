import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        # 상위 객체 생성, 생성자 호출
        super().__init__()
        self.initUI()

    ## Confirm

    def initUI(self):
        btn = QPushButton('push me!', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.resize(500, 500)
        self.setWindowTitle('Hello')
        self.show()

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "닫을꾸야?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

# 어플리케이션 오브젝트 생성
app = QApplication(sys.argv)
w = Exam()
# 이벤트처리를 위한 루프 실행
sys.exit(app.exec_())