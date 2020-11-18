from PyQt5 import QtWidgets

import conexion
import var


class Clients():

    @staticmethod
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
                var.sex = 'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def selPago():
        try:
            pay = []
            for i, data in enumerate(var.ui.chkGroupPago.buttons()):
                if var.ui.chkEfectivo.isChecked():
                    pay.append('Efectivo')
                if var.ui.chkTarjeta.isChecked():
                    pay.append('Tarjeta')
                if var.ui.chkTransferencia.isChecked():
                    pay.append('Transferencia')
                print(pay)
                return pay
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

    @staticmethod
    def selectProvincia(prov):
        try:
            var.vpro = prov
            return prov
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editFecha.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def abrirCalendar():
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def altaCliente():
        '''
        Cargara los clientes en la tabla
        '''

        try:
            # Preparamos el registro
            newCli = []

            k = 0
            for i in var.listaEditClients:
                newCli.append(i.text())  # cargamos los valores que hay en los editLine

            newCli.append(var.vpro)
            newCli.append(var.sex)
            newCli.append(Clients.selPago())

            print(newCli)


            for x in var.listaEditClients:
                print(x.text())

            # aqui empieza como trabajar con la TableWidget
            if Clients.validarDNI(var.ui.editDNI.text()) and var.listaEditClients:

                if conexion.Conexion.crearCliente(newCli):
                    Clients.limpiarCliente()

            else:
                print('Faltan datos')


        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def cargarClientes():
        try:
            fila = var.ui.tablaCli.selectedItems()
            client = [var.ui.editDNI, var.ui.editApellido, var.ui.editNombre]
            if fila:
                fila = [dato.text() for dato in fila]
                print(fila)
                i=0
                for i, dato in enumerate(client):
                    dato.setText(fila[i])
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def limpiarCliente():
            try:
                for i in range(len(var.listaEditClients)):
                    var.listaEditClients[i].setText('')
                var.ui.rbtGroupSex.setExclusive(False)
                for dato in var.chkpago:
                    dato.setChecked(False)
                for data in var.rbtSex:
                    data.setChecked(False)
                var.ui.cmbProvincia.setCurrentIndex(0)
                var.ui.lblValido.setText('')
            except Exception as error:
                print('Error: %s' % str(error))