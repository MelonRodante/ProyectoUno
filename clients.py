import var

class Clients():
    def validarDNI(dni):
        try:
            tabla = "TRWAGMYFDPXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"

            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control
            return False


        except:
            print('error en la aplicacion')
            return None

    @staticmethod
    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                print('Has elegido femenino')
            if var.ui.rbtMasc.isChecked():
                print('Has elegido masculino')
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def selPago():
        try:
            if var.ui.chkEfectivo.isChecked():
                print('Pagas en efectivo')
            if var.ui.chkTarjeta.isChecked():
                print('Pagas con tarjeta')
            if var.ui.chkTransferencia.isChecked():
                print('Pagas con transferencia')
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def cargarProvincias():
        try:
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            for i in prov:
                var.ui.cmbProvincia.addItem(i)
        except Exception as error:
            print('Error: %s' % str(error))

    def selectProvincia(prov):
        try:
            print('Has seleccionado la provincia de', prov)
            return prov
        except Exception as error:
            print('Error: %s' % str(error))

    def cargaFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editFecha.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error: %s' % str(error))