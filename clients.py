from PyQt5 import QtWidgets

import conexion
import events
import main
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
                return 'Mujer'
            if var.ui.rbtMasc.isChecked():
                return 'Hombre'
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def selPago():
        try:
            pay = []
            for data in enumerate(var.ui.chkGroupPago.buttons()):
                if var.ui.chkEfectivo.isChecked():
                    pay.append('Efectivo')
                if var.ui.chkTarjeta.isChecked():
                    pay.append('Tarjeta')
                if var.ui.chkTransferencia.isChecked():
                    pay.append('Transferencia')
                return pay
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def cargarProvincias():
        try:
            for i in var.prov:
                var.ui.cmbProvincia.addItem(i)
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def selectProvincia():
        try:
            return var.ui.cmbProvincia.currentText()
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def abrirCalendar():
        try:
            dlgCalendar = main.DialogCalendar()
            dlgCalendar.exec_()
        except Exception as error:
            print('Error: %s ' % str(error))

    @staticmethod
    def cargarClientes():

        try:
            fila = var.ui.tablaCli.selectedItems()
            cliente = conexion.Conexion.cargarCli(fila[0].text())

            if cliente:

                i = 0
                for i, dato in enumerate(var.listaEditClients):
                    dato.setText(cliente[i])

                i += 1
                var.ui.cmbProvincia.setCurrentIndex(var.prov.index(cliente[i]))

                i += 1
                if cliente[i] == 'Hombre':
                    var.ui.rbtMasc.setChecked(True)
                else:
                    var.ui.rbtFem.setChecked(True)

                i += 1
                tiposPago = ['Tarjeta', 'Efectivo', 'Transferencia']

                for x, dato in enumerate(var.chkpago):
                    dato.setChecked(cliente[i].__contains__(tiposPago[x]))

                i += 1
                var.ui.spinEdad.setValue(cliente[i])


        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def altaCliente():
        '''
        Cargara los clientes en la tabla
        '''

        try:

            newCli = []

            for i in var.listaEditClients:
                newCli.append(i.text())

            newCli.append(Clients.selectProvincia())
            newCli.append(Clients.selSexo())
            newCli.append(Clients.selPago())

            newCli.append(var.ui.spinEdad.value())

            valido = True
            for i in newCli:
                if not i:
                    valido = False
                    break;

            if valido:
                if Clients.validarDNI(var.ui.editDNI.text()):
                    conexion.Conexion.crearCli(newCli)
                else:
                    events.Eventos.DialoAviso('Error: DNI no valido')
            else:
                events.Eventos.DialoAviso('Error: Faltan datos')
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def bajaCliente():
        try:
            dni = var.ui.editDNI.text()
            if conexion.Conexion.cargarCli(dni):
                conf = main.DialogConfirmar("¿Desea eliminar al empleado de la base de datos?", conexion.Conexion.bajaCli)
                conf.show()
                conf.exec_()
            else:
                events.Eventos.DialoAviso('Error: No existe ningun empleado con ese DNI')
        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def modifCliente():
        try:
            newdata = []

            for i in var.listaEditClients:
                newdata.append(i.text())  # cargamos los valores que hay en los editLine

            newdata.append(Clients.selectProvincia())
            newdata.append(Clients.selSexo())
            newdata.append(Clients.selPago())

            newdata.append(var.ui.spinEdad.value())

            valido = True
            for i in newdata:
                if not i:
                    valido = False
                    break;

            if valido:
                conexion.Conexion.modificarCli(newdata)
            else:
                events.Eventos.DialoAviso('Error: Faltan datos')

        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def limpiarCliente():
        try:
            for i in range(len(var.listaEditClients)):
                var.listaEditClients[i].setText('')

            var.ui.lblValido.setText('')

            var.ui.rbtGroupSex.setExclusive(False)
            for data in var.rbtSex:
                data.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)

            for dato in var.chkpago:
                dato.setChecked(False)

            var.ui.cmbProvincia.setCurrentIndex(0)

            var.ui.spinEdad.setValue(18)

        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def buscarCliente():
        conexion.Conexion.buscarCli(var.ui.editDNI.text())
