# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vensalir.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venSalir(object):
    def setupUi(self, venSalir):
        venSalir.setObjectName("venSalir")
        venSalir.setWindowModality(QtCore.Qt.WindowModal)
        venSalir.resize(400, 120)
        venSalir.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(venSalir)
        self.buttonBox.setGeometry(QtCore.QRect(30, 70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.lblMensajeSalir = QtWidgets.QLabel(venSalir)
        self.lblMensajeSalir.setGeometry(QtCore.QRect(80, 30, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lblMensajeSalir.setFont(font)
        self.lblMensajeSalir.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMensajeSalir.setObjectName("lblMensajeSalir")
        self.lblImgSalir = QtWidgets.QLabel(venSalir)
        self.lblImgSalir.setGeometry(QtCore.QRect(30, 10, 51, 51))
        self.lblImgSalir.setText("")
        self.lblImgSalir.setPixmap(QtGui.QPixmap(":/aviso/aviso.png"))
        self.lblImgSalir.setScaledContents(False)
        self.lblImgSalir.setObjectName("lblImgSalir")

        self.retranslateUi(venSalir)
        self.buttonBox.accepted.connect(venSalir.accept)
        self.buttonBox.rejected.connect(venSalir.reject)
        QtCore.QMetaObject.connectSlotsByName(venSalir)

    def retranslateUi(self, venSalir):
        _translate = QtCore.QCoreApplication.translate
        venSalir.setWindowTitle(_translate("venSalir", "Dialog"))
        self.lblMensajeSalir.setText(_translate("venSalir", "¿Está seguro de que desea salir de la aplicación?"))
import aviso_rc
