from PyQt5.QtWidgets import QDialog,QPushButton

class C_Dos(QDialog):
    def __init__(self,app):
        QDialog.__init__(self)

        boton = QPushButton(self)
        boton.setText("Abrir")
        boton.clicked.connect(app.abrirMainWindow)

