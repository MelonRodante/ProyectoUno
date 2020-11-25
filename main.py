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
        conexion.Conexion.mostrarClientes()

        '''
        Conexion con los eventos
        '''


        '''Otros eventos'''
        QtWidgets.QAction(self).triggered.connect(self.close)  # Cerrar al pulsar la X de la ventana

        var.ui.editDNI.editingFinished.connect(events.Eventos.ValidoDni)

        clients.Clients.cargarProvincias()

        var.ui.tablaCli.clicked.connect(clients.Clients.cargarClientes)
        var.ui.tablaCli.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        header = var.ui.tablaCli.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        '''Botones'''
        var.ui.btnCalendar.clicked.connect(clients.Clients.abrirCalendar)

        var.ui.btnAlta.clicked.connect(clients.Clients.altaCliente)
        var.ui.btnBaja.clicked.connect(clients.Clients.bajaCliente)
        var.ui.btnModificar.clicked.connect(clients.Clients.modifCliente)
        var.ui.btnLimpiar.clicked.connect(clients.Clients.limpiarCliente)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)

        '''MenuBar'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

    def closeEvent(self, event):
        events.Eventos.SalirBoton(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    #window.showMaximized()
    window.show()
    sys.exit(app.exec_())

