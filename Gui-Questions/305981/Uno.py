from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

class Main(QMainWindow):
    def __init__(self,app):
        QMainWindow.__init__(self)

        boton = QPushButton(self)
        boton.setText("Abrir")
        boton.clicked.connect(app.abrirDialog)
