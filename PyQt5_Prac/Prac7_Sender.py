import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class Exam(QMainWindow):
    def __init__(self):
        # 상위 객체 생성, 생성자 호출
        super().__init__()
        self.initUI()

    ## 버튼 누르면 상태표시줄에 메세지 표시하기

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()     # 호출 한 객체
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':
    # 어플리케이션 오브젝트 생성
    app = QApplication(sys.argv)
    w = Exam()
    # 이벤트처리를 위한 루프 실행
    sys.exit(app.exec_())