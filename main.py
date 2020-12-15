import conexion
from vencalendar import *
from ventana import *
from vendialog import *
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore, QtPrintSupport
import sys, var, events, clients, locale

locale.setlocale(locale.LC_ALL, 'es-ES')

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        self.dlgcalendar = Ui_venCalendar()
        self.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        self.dlgcalendar.calendar.setSelectedDate(QtCore.QDate(anoactual,mesactual,diaactual))
        self.dlgcalendar.calendar.clicked.connect(self.cargarFecha)

    def cargarFecha(self):
        try:
            date = self.dlgcalendar.calendar.selectedDate()
            data = ('{0}/{1}/{2}'.format(date.day(),date.month(),date.year()))
            var.ui.editFecha.setText(str(data))
            self.close()
        except Exception as error:
            print('Error: %s' % str(error))

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        self.ventana = Ui_venDialog()
        self.ventana.setupUi(self)
        self.ventana.retranslateUi(self, '¿Esta seguro de que desea salir de la aplicacion?', 'Si', 'No')
        self.ventana.btnAceptar.clicked.connect(self.Salir)
        self.ventana.btnCancelar.clicked.connect(self.close)

    def Salir(self):
        sys.exit(0)

class DialogAviso(QtWidgets.QDialog):
    def __init__(self, msg):
        super(DialogAviso, self).__init__()
        self.ventana = Ui_venDialog()
        self.ventana.setupUi(self)
        self.ventana.retranslateUi(self, msg, 'Aceptar')
        self.ventana.btnAceptar.clicked.connect(self.close)
        self.ventana.btnCancelar.hide()

class DialogConfirmar(QtWidgets.QDialog):
    def __init__(self, msg, funcionAceptar):
        super(DialogConfirmar, self).__init__()
        self.ventana = Ui_venDialog()
        self.ventana.setupUi(self)
        self.ventana.retranslateUi(self, msg, 'Si', 'No')
        self.funcionAceptar = funcionAceptar
        self.ventana.btnAceptar.clicked.connect(self.aceptar)
        self.ventana.btnCancelar.clicked.connect(self.close)

    def aceptar(self, funcionAceptar):
        self.funcionAceptar()
        self.close()

class DialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(DialogAbrir, self).__init__()

class DialogImprimir(QtPrintSupport.QPrintDialog):
    def __init__(self):
        super(DialogImprimir, self).__init__()

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

        labelFecha = QtWidgets.QLabel(datetime.now().strftime("%d %B %Y"))
        var.ui.statusbar.addPermanentWidget(labelFecha)

        '''
        Definimos variables
        '''
        var.listaEditClients = [var.ui.editDNI, var.ui.editApellido, var.ui.editNombre, var.ui.editFecha, var.ui.editDireccion]

        var.rbtSex = (var.ui.rbtMasc, var.ui.rbtFem)
        var.chkpago = (var.ui.chkTarjeta, var.ui.chkEfectivo, var.ui.chkTransferencia)



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
        var.ui.btnBuscar.clicked.connect(clients.Clients.buscarCliente)
        var.ui.btnRecargar.clicked.connect(conexion.Conexion.mostrarClientes)

        var.ui.btnAlta.clicked.connect(clients.Clients.altaCliente)
        var.ui.btnBaja.clicked.connect(clients.Clients.bajaCliente)
        var.ui.btnModificar.clicked.connect(clients.Clients.modifCliente)
        var.ui.btnLimpiar.clicked.connect(clients.Clients.limpiarCliente)
        var.ui.btnSalir.clicked.connect(events.Eventos.AbrirDialogSalir)

        '''MenuBar'''
        var.ui.actionAbrir.triggered.connect(events.Eventos.DialogoAbrir)
        var.ui.actionImprimir.triggered.connect(events.Eventos.DialogoImprimir)
        var.ui.actionSalir.triggered.connect(events.Eventos.AbrirDialogSalir)

        '''ToolBar'''
        var.ui.toolbarAbrir.triggered.connect(events.Eventos.DialogoAbrir)
        var.ui.toolbarImprimir.triggered.connect(events.Eventos.DialogoImprimir)
        var.ui.toolbarSalir.triggered.connect(events.Eventos.AbrirDialogSalir)

    def closeEvent(self, event):
        events.Eventos.AbrirDialogSalir()
        event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    #window.showMaximized()
    window.show()
    sys.exit(app.exec_())

