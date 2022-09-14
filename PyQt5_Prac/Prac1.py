import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        # 상위 객체 생성, 생성자 호출
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('ain', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('툴팁이예용')
        btn.move(20, 30)

        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('Hello')
        self.show()

# 어플리케이션 오브젝트 생성
app = QApplication(sys.argv)
w = Exam()
# 이벤트처리를 위한 루프 실행
sys.exit(app.exec_())