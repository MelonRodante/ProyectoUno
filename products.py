import conexion
import events
import var

class Products():

    @staticmethod
    def cargarPro():
        try:
            fila = var.ui.tablaProductos.selectedItems()
            producto = conexion.Conexion.cargarPro(fila[0].text())

            if producto:
                var.ui.editProCodigo.setText(str(producto[0]))
                var.ui.editProNombre.setText(str(producto[1]))
                var.ui.spinPrecio.setValue(producto[2])
        except Exception as e:
            print('Error:', e)

    @staticmethod
    def altaPro():
        producto = []

        if var.ui.editProNombre.text() != '':
            producto.append(var.ui.editProNombre.text())
            producto.append(var.ui.spinPrecio.value())
            conexion.Conexion.altaPro(producto)
        else:
            events.Eventos.DialoAviso('Error: El producto debe tener nombre')

    @staticmethod
    def bajaPro():
        if var.ui.editProCodigo.text() != '':
            conexion.Conexion.bajaPro()
        else:
            events.Eventos.DialoAviso('Error: Seleccione un producto a dar de baja')

    @staticmethod
    def modificarPro():
        try:
            producto = []

            if var.ui.editProCodigo.text() == '':
                events.Eventos.DialoAviso('Error: Seleccione un producto a modificar')
            elif var.ui.editProNombre.text() == '':
                events.Eventos.DialoAviso('Error: El producto debe tener nombre')
            else:
                producto.append(var.ui.editProCodigo.text())
                producto.append(var.ui.editProNombre.text())
                producto.append(var.ui.spinPrecio.value())

                conexion.Conexion.modificarPro(producto)


        except Exception as error:
            print('Error: %s' % str(error))

    @staticmethod
    def limpiarPro():
        var.ui.editProCodigo.setText('')
        var.ui.editProNombre.setText('')
        var.ui.spinPrecio.setValue(0)
