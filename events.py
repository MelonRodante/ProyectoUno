import var, sys, clients

class Eventos():

    '''
    Eventos generales
    '''

    def Salir(event):
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec_():
                sys.exit()
            else:
                var.dlgsalir.close()
                event.ignore()
        except Exception as error:
            print('El error es %s' % str(error))

    @staticmethod
    def ValidoDni():
        try:
            dni = var.ui.editDNI.text()
            if clients.Clients.validarDNI(dni):
                var.ui.lblValido.setStyleSheet('QLabel {color: green}')
                var.ui.lblValido.setText('V')
                var.ui.editDNI.setText(dni.upper())
            else:
                var.ui.lblValido.setStyleSheet('QLabel {color: red}')
                var.ui.lblValido.setText('X')
                var.ui.editDNI.setText(dni.upper())
        except Exception as error:
            print('Error: %s ' % str(error))