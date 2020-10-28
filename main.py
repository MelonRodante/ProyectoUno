from ventana import *
import sys, var, events


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

        '''
        Conexion con los eventos
        '''

        '''Otros eventos'''
        var.ui.editDNI.editingFinished.connect(events.Eventos.ValidoDni)

        '''Botones'''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)

        '''MenuBar'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

