from PyQt5.QtWidgets import QApplication

#Ninguno de los dos modulos se conoce
from Uno import Main
from Dos import C_Dos

class App():
    def __init__(self):
        self.mainWindow = Main(self)
        self.mainWindow.setWindowTitle('Uno Main Window')
        self.dosDialog = C_Dos(self)
        self.dosDialog.setWindowTitle('Dos Dialog')
        self.mainWindow.show()
        self.mainWindow.resize(500,400)

    def abrirDialog(self):
        print("openning dialog")
        self.dosDialog.show()
        self.dosDialog.resize(500,400)
        print("closing main window")
        self.mainWindow.close()

    def abrirMainWindow(self):
        print("openning main window")
        self.mainWindow.show()
        print("closing dos dialog")
        self.dosDialog.close()

def main():
    qapp = QApplication([])
    app = App()
    qapp.exec_()


if __name__ == "__main__":
    main()

