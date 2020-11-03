import var, sys, clients

class Eventos():

    '''
    Eventos generales
    '''

    @staticmethod
    def Salir():
        try:
            var.avisosalir.show()
            if var.avisosalir.exec_():
                sys.exit()
            else:
                var.avisosalir.close()
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