import conexion
from vencalendar import *
from ventana import *
from vensalir import *
from datetime import datetime
import sys, var, events, clients


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_venCalendar()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.calendar.setSelectedDate(QtCore.QDate(anoactual,mesactual,diaactual))
        var.dlgcalendar.calendar.clicked.connect(clients.Clients.cargarFecha)


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_venSalir()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.buttonBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)
        #var.dlgsalir.buttonBox.button(QtWidgets.QDialogButtonBox.No).clicked.connect(events.Eventos.Salir)


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

        '''
        Definimos variables
        '''
        var.dlgcalendar = DialogCalendar()
        var.dlgsalir = DialogSalir()

        var.listaEditClients = [var.ui.editDNI, var.ui.editApellido, var.ui.editNombre, var.ui.editFecha, var.ui.editDireccion]

        var.rbtSex = (var.ui.rbtMasc, var.ui.rbtFem)
        var.chkpago = (var.ui.chkEfectivo, var.ui.chkTarjeta, var.ui.chkTransferencia)

        '''
        Conexion con la base de datos       
        '''
        conexion.Conexion.conectardb(var.filedb)

        '''
        Conexion con los eventos
        '''


        '''Otros eventos'''
        QtWidgets.QAction(self).triggered.connect(self.close)  # Cerrar al pulsar la X de la ventana

        var.ui.editDNI.editingFinished.connect(events.Eventos.ValidoDni)

        clients.Clients.cargarProvincias()
        var.ui.cmbProvincia.activated[str].connect(clients.Clients.selectProvincia)

        var.ui.tablaCli.clicked.connect(clients.Clients.cargarClientes)
        var.ui.tablaCli.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        '''Botones'''
        var.ui.btnCalendar.clicked.connect(clients.Clients.abrirCalendar)

        var.ui.btnAlta.clicked.connect(clients.Clients.altaCliente)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)


        '''Radio Buttons'''
        for i in var.rbtSex:
            i.toggled.connect(clients.Clients.selSexo)

        '''Check Box'''
        for i in var.chkpago:
            i.stateChanged.connect(clients.Clients.selPago)

        '''MenuBar'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

    def closeEvent(self, event):
        events.Eventos.SalirBoton(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec_())

