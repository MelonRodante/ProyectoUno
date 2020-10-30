import clients
from ventana import *
import sys, var, events


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

        '''
        Definimos variables
        '''
        var.rbtSex = (var.ui.rbtMasc, var.ui.rbtFem)
        var.chkPago = (var.ui.chkEfectivo, var.ui.chkTarjeta, var.ui.chkTransferencia)


        '''
        Conexion con los eventos
        '''

        '''Otros eventos'''
        var.ui.editDNI.editingFinished.connect(events.Eventos.ValidoDni)

        clients.Clients.cargarProvincias()
        var.ui.cmbProvincia.activated[str].connect(clients.Clients.selectProvincia)

        '''Botones'''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)

        '''Radio Buttons'''
        for i in var.rbtSex:
            i.toggled.connect(clients.Clients.selSexo)

        '''Check Box'''
        for i in var.chkPago:
            i.stateChanged.connect(clients.Clients.selPago)
        '''MenuBar'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

