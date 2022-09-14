import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QMenu, qApp
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        # 상위 객체 생성, 생성자 호출
        super().__init__()
        self.initUI()

        ## 메뉴바 만들기

    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("안녕하세요")

        menu = self.menuBar()               # 메뉴 생성
        menu_file = menu.addMenu('File')    # 그룹 생성
        menu_edit = menu.addMenu('Edit')    # 그룹 생성
        menu_view = menu.addMenu('View')    # 그룹 생성
        
        file_exit = QAction('Exit', self)   # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')     # 단축키 설정
        file_exit.setStatusTip("누르면 꺼져용")
        file_exit.triggered.connect(QCoreApplication.instance().quit)       # QCoreApplication.instance().quit ==> qApp.quit 으로 변경해도 같은 기능

        file_new_txt = QAction("text", self)
        file_new_py = QAction("python", self)

        view_stat = QAction('상태표시줄', self, checkable = True)
        view_stat.setChecked(True)
        view_stat.triggered.connect(self.tglStat)

        file_new = QMenu('New', self)       # 서브 그룹

        file_new.addAction(file_new_txt)    # 서브 메뉴 추가
        file_new.addAction(file_new_py)     # 서브 메뉴 추가

        menu_file.addMenu(file_new)         # 주메뉴 등록
        menu_file.addAction(file_exit)      # 주메뉴 등록
        menu_view.addAction(view_stat)

        self.resize(450,400)
        self.show()

    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()


    def contextMenuEvent(self, QContextMenuEvent):
        cm = QMenu(self)

        quit = cm.addAction("Quit")
        action = cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quit:
            qApp.quit()     # ==QCoreApplication.instance().quit

# 어플리케이션 오브젝트 생성
app = QApplication(sys.argv)
w = Exam()
# 이벤트처리를 위한 루프 실행
sys.exit(app.exec_())