import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        # 상위 객체 생성, 생성자 호출
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(450,400)
        self.show()

# 어플리케이션 오브젝트 생성
app = QApplication(sys.argv)
w = Exam()
# 이벤트처리를 위한 루프 실행
sys.exit(app.exec_())