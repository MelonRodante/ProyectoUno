from vencalendar import *
from ventana import *
from vensalir import *
from datetime import datetime
import sys, var, events, clients


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

        var.avisosalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()

        '''
        Conexion con los eventos
        '''
        QtWidgets.QAction(self).triggered.connect(self.close) #Cerrar al pulsar la X de la ventana



        '''Otros eventos'''
        var.ui.editDNI.editingFinished.connect(events.Eventos.ValidoDni)
        clients.Clients.cargarProvincias()
        var.ui.cmbProvincia.activated[str].connect(clients.Clients.selectProvincia)

        '''Botones'''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.btnCalendar.clicked.connect(clients.Clientes.abrirCalendar)

        '''Radio Buttons'''
        for i in var.rbtSex:
            i.toggled.connect(clients.Clients.selSexo)

        '''Check Box'''
        for i in var.chkPago:
            i.stateChanged.connect(clients.Clients.selPago)

        '''MenuBar'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

    def close(self, event):
        events.Eventos.Salir()


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisosalir = Ui_venSalir()
        var.avisosalir.setupUi(self)
        var.avisosalir.buttonBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)
        var.avisosalir.buttonBox.button(QtWidgets.QDialogButtonBox.No).clicked.connect(events.Eventos.Salir)


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_venCalendar
        var.dlgcalendar.setupUi(self)
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.calendar.setSelectedDate(QtCore.QDate(anoactual,mesactual,1))
        var.dlgcalendar.calendar.clicked.connect(clients.Clients.cargarFecha)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())

