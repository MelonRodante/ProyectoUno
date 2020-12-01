from PyQt5 import QtSql, QtWidgets

import events
import main
import var
from clients import Clients


class Conexion:

    @staticmethod
    def conectardb(filename):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)

        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexion.\n' 'Haz click para cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexion establecida')
            return True

    @staticmethod
    def mostrarClientes():
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            var.ui.tablaCli.setRowCount(0)
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                var.ui.tablaCli.setRowCount(index + 1)
                var.ui.tablaCli.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tablaCli.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tablaCli.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    @staticmethod
    def cargarCli(dni):
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre, fechaalta, direccion, provincia, sexo, formaspago, edad from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            if query.next():
                cliente = []
                for i in range(9):
                    cliente.append(query.value(i))
                return cliente
            else:
                return None
        else:
            print("Error cargando cliente: ", query.lastError().text())

    @staticmethod
    def crearCli(cliente):
        query = QtSql.QSqlQuery()
        query.prepare('insert into clientes (dni, apellidos, nombre, fechaalta, direccion, provincia, sexo, formaspago, edad)'
                      'VALUES (:dni, :apellidos, :nombre, :fechaalta, :direccion, :provincia, :sexo, :formaspago, :edad)')
        query.bindValue(':dni',         str(cliente[0]))
        query.bindValue(':apellidos',   str(cliente[1]))
        query.bindValue(':nombre',      str(cliente[2]))
        query.bindValue(':fechaalta',   str(cliente[3]))
        query.bindValue(':direccion',   str(cliente[4]))
        query.bindValue(':provincia',   str(cliente[5]))
        query.bindValue(':sexo',        str(cliente[6]))
        query.bindValue(':formaspago',  str(cliente[7]))
        query.bindValue(':edad', cliente[8])

        if query.exec_():
            Conexion.mostrarClientes()
            Clients.limpiarCliente()
            var.ui.statusbar.showMessage('Cliente con DNI ' + var.ui.editDNI.text() + ' dado de alta')

        else:
            dialog = main.DialogAviso('Error: Ya existe un cliente con el ese DNI')
            dialog.show()
            dialog.exec_()

    @staticmethod
    def bajaCli():

        dni = var.ui.editDNI.text()

        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)


        if query.exec_():
            var.ui.statusbar.showMessage('Cliente con DNI ' + dni + ' dado de baja')
            Conexion.mostrarClientes()
            Clients.limpiarCliente()
        else:
            events.Eventos.DialoAviso('Error: No existe ningun empleado con ese DNI')

    @staticmethod
    def modificarCli(newdata):

        query = QtSql.QSqlQuery()
        query.prepare('update clientes set apellidos=:apellidos, nombre=:nombre, fechaalta=:fechaalta, direccion=:direccion, provincia=:provincia, sexo=:sexo, formaspago=:formaspago, edad=:edad where dni = :dni')
        query.bindValue(':dni',         str(newdata[0]))
        query.bindValue(':apellidos',   str(newdata[1]))
        query.bindValue(':nombre',      str(newdata[2]))
        query.bindValue(':fechaalta',    str(newdata[3]))
        query.bindValue(':direccion',   str(newdata[4]))
        query.bindValue(':provincia',   str(newdata[5]))
        query.bindValue(':sexo',        str(newdata[6]))
        query.bindValue(':formaspago',  str(newdata[7]))
        query.bindValue(':edad', newdata[8])

        if query.exec_() and Conexion.cargarCli(str(newdata[0])):
            Conexion.mostrarClientes()
            Clients.limpiarCliente()
            var.ui.statusbar.showMessage('Datos del cliente con DNI ' + newdata[0] + ' modificados')
        else:
            events.Eventos.DialoAviso('Error: No existe ningun empleado con ese DNI')

