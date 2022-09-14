import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout

class Exam(QWidget):
    def __init__(self):
        # 상위 객체 생성, 생성자 호출
        super().__init__()
        self.initUI()

    ## 슬라이더 움직임에 따라 숫자 표시하는 이벤트
    ## ESC키로 창 끄기

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)      # 슬라이더 가로로 설정

        # 배치
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()

    # 재정의 / esc키 창 꺼짐
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    # 어플리케이션 오브젝트 생성
    app = QApplication(sys.argv)
    w = Exam()
    # 이벤트처리를 위한 루프 실행
    sys.exit(app.exec_())