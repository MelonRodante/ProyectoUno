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
        var.avisosalir = Ui_venSalir()
        var.avisosalir.setupUi(self)
        var.avisosalir.buttonBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)
        var.avisosalir.buttonBox.button(QtWidgets.QDialogButtonBox.No).clicked.connect(events.Eventos.Salir)


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)

        '''
        Definimos variables
        '''
        var.dlgcalendar = DialogCalendar()
        var.avisosalir = DialogSalir()

        var.rbtSex = (var.ui.rbtMasc, var.ui.rbtFem)
        var.chkpago = (var.ui.chkEfectivo, var.ui.chkTarjeta, var.ui.chkTransferencia)


        '''
        Conexion con los eventos
        '''


        '''Otros eventos'''
        QtWidgets.QAction(self).triggered.connect(self.close)  # Cerrar al pulsar la X de la ventana
        var.ui.editDNI.editingFinished.connect(events.Eventos.ValidoDni)
        clients.Clients.cargarProvincias()
        var.ui.cmbProvincia.activated[str].connect(clients.Clients.selectProvincia)

        '''Botones'''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.btnCalendar.clicked.connect(clients.Clients.abrirCalendar)

        '''Radio Buttons'''
        for i in var.rbtSex:
            i.toggled.connect(clients.Clients.selSexo)

        '''Check Box'''
        for i in var.chkpago:
            i.stateChanged.connect(clients.Clients.selPago)

        '''MenuBar'''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

    def closeEvent(self, event):
        events.Eventos.Salir()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec_())

