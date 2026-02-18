import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QStackedWidget, QLabel
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InterfaceMenu avec deux pages différents")
        self.resize(600, 400)

        central = QWidget()
        main_layout = QHBoxLayout(central)

        # Supprime les espaces entre le box layout et la bordure de la fenetre
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Menu gauche 
        menu = QWidget()
        menu_layout = QVBoxLayout(menu)
        
        menu.setContentsMargins(0, 0, 0, 0)

        btn1 = QPushButton("Page 1")
        btn2 = QPushButton("Page 2")
        menu_layout.addWidget(btn1)
        menu_layout.addWidget(btn2)
        menu_layout.addStretch()

        # suppression des espaces entre les deux boutons
        menu_layout.setSpacing(0)
        menu_layout.setContentsMargins(0, 0, 0, 0)

        # Pages 
        self.stack = QStackedWidget()

        page1 = QWidget()
        p1_layout = QVBoxLayout(page1)
        p1_layout.addWidget(QLabel("Page 1"))

        page2 = QWidget()
        p2_layout = QVBoxLayout(page2)
        p2_layout.addWidget(QLabel("Page 2"))

        self.stack.addWidget(page1)  
        self.stack.addWidget(page2)  

        # Connexions
        btn1.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        btn2.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        # Assemblage 
        main_layout.addWidget(menu)
        main_layout.addWidget(self.stack)

        self.setCentralWidget(central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    try:
        with open("styles/styles.qss", "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        pass
    sys.exit(app.exec())