from PyQt5 import QtWidgets

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
                var.sex = 'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def selPago():
        try:
            if var.ui.chkEfectivo.isChecked():
                var.pay.append('Efectivo')
            if var.ui.chkTarjeta.isChecked():
                var.pay.append('Tarjeta')
            if var.ui.chkTransferencia.isChecked():
                var.pay.append('Transferencia')
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
            var.vpro = prov
            return prov
        except Exception as error:
            print('Error: %s' % str(error))

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editFecha.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error: %s' % str(error))

    def abrirCalendar(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def showClientes():
        '''
        Cargara los clientes en la tabla
        '''

        try:
            # Preparamos el registro
            newCli = []
            clitab = []  # sera lo que carguemos en la tabla

            k = 0
            for i in var.listaEditClients:
                newCli.append(i.text())  # cargamos los valores que hay en los editLine
                if k < 3:
                    clitab.append(i.text())
                    k += 1

            newCli.append(var.vpro)

            newCli.append(var.sex)

            var.pay = set(var.pay)
            for j in var.pay:
                newCli.append(j)


            print(newCli)
            print(clitab)

            # aqui empieza como trabajar con la TableWidget

            row = 0
            column = 0

            var.ui.tablaCli.insertRow(row)
            for registro in clitab:
                cell = QtWidgets.QTableWidgetItem(registro)
                var.ui.tablaCli.setItem(row, column, cell)
                column += 1

            Clients.limpiarCliente()

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