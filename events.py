import var, sys, clients, main

class Eventos():

    '''
    Eventos generales
    '''

    @staticmethod
    def AbrirDialogSalir():
        try:
            dialog = main.DialogSalir()
            dialog.show()
            dialog.exec_()
        except Exception as error:
            print('El error es %s' % str(error))

    @staticmethod
    def AbrirAbout():
        try:
            about = main.DialogAbout()
            about.show()
            about.exec_()
        except Exception as error:
            print('El error es %s' % str(error))

    @staticmethod
    def ValidoDni():
        try:
            dni = var.ui.editDNI.text()
            if dni != '':
                if clients.Clients.validarDNI(dni):
                    var.ui.lblValido.setStyleSheet('QLabel {color: green}')
                    var.ui.lblValido.setText('V')
                    var.ui.editDNI.setText(dni.upper())
                else:
                    var.ui.lblValido.setStyleSheet('QLabel {color: red}')
                    var.ui.lblValido.setText('X')
                    var.ui.editDNI.setText(dni.upper())
            else:
                var.ui.lblValido.setText('')
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def DialoAviso(msg):
        var.ui.statusbar.showMessage(msg)
        dialog = main.DialogAviso(msg)
        dialog.show()
        dialog.exec_()


    @staticmethod
    def DialogoAbrir():
        dialog = main.DialogAbrir()
        dialog.show()
        dialog.exec_()

    @staticmethod
    def DialogoImprimir():
        dialog = main.DialogImprimir()
        dialog.show()
        dialog.exec_()