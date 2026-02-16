from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget
import sys


# On définit une classe pour notre nouvelle fenêtre.
class MyWindow(QMainWindow):

    # Le constructeur de notre classe de fenêtre.
    def __init__(self):
        # On initialise la fenêtre, notamment en rappelant le constructeur parent.
        super().__init__()
        self.setWindowTitle("Ma première fenêtre Qt avec Python")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(400, 300)

        # On crée un widget représentant la zone centrale de la fenêtre.
        centralWidget = QWidget()
        # On y ajoute un premier bouton.
        self.__button1 = QPushButton("Premier bouton", centralWidget)
        self.__button1.setGeometry(20, 20, 200, 35)
        self.__button1.clicked.connect(self.doSomething)

        # On fait de même pour un second bouton.
        self.__button2 = QPushButton("Second bouton", centralWidget)
        self.__button2.setGeometry(20, 60, 200, 35)
        self.__button2.clicked.connect(self.doSomething)

        # On injecte le composant en tant que "widget central".
        self.setCentralWidget(centralWidget)

    # Un gestionnaire d'événements (voir les connexions ci-dessus).
    def doSomething(self):
        print(self.sender().text(), "cliqué")


if __name__ == "__main__":
    # On crée un objet représentant l'application Qt.
    app = QApplication(sys.argv)

    # On crée une instance de notre fenêtre et on l'affiche.
    myWindow = MyWindow()
    myWindow.show()

    # On lance le système Qt.
    sys.exit(app.exec())