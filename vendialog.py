# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vendialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venDialog(object):
    def setupUi(self, venDialog):
        venDialog.setObjectName("venDialog")
        venDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        venDialog.setEnabled(True)
        venDialog.resize(182, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(venDialog.sizePolicy().hasHeightForWidth())
        venDialog.setSizePolicy(sizePolicy)
        venDialog.setMinimumSize(QtCore.QSize(0, 100))
        venDialog.setMaximumSize(QtCore.QSize(16777215, 100))
        venDialog.setSizeGripEnabled(False)
        venDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(venDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setSpacing(6)
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.lblImgSalir = QtWidgets.QLabel(venDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImgSalir.sizePolicy().hasHeightForWidth())
        self.lblImgSalir.setSizePolicy(sizePolicy)
        self.lblImgSalir.setText("")
        self.lblImgSalir.setPixmap(QtGui.QPixmap(":/aviso/aviso.png"))
        self.lblImgSalir.setScaledContents(False)
        self.lblImgSalir.setObjectName("lblImgSalir")
        self.horizontalLayout1.addWidget(self.lblImgSalir)
        self.lblMensajeSalir = QtWidgets.QLabel(venDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMensajeSalir.sizePolicy().hasHeightForWidth())
        self.lblMensajeSalir.setSizePolicy(sizePolicy)
        self.lblMensajeSalir.setMinimumSize(QtCore.QSize(0, 0))
        self.lblMensajeSalir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.lblMensajeSalir.setFont(font)
        self.lblMensajeSalir.setText("")
        self.lblMensajeSalir.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblMensajeSalir.setObjectName("lblMensajeSalir")
        self.horizontalLayout1.addWidget(self.lblMensajeSalir)
        self.gridLayout.addLayout(self.horizontalLayout1, 0, 0, 1, 1)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout2.addItem(spacerItem)
        self.btnAceptar = QtWidgets.QPushButton(venDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAceptar.sizePolicy().hasHeightForWidth())
        self.btnAceptar.setSizePolicy(sizePolicy)
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnGrpAcpCanc = QtWidgets.QButtonGroup(venDialog)
        self.btnGrpAcpCanc.setObjectName("btnGrpAcpCanc")
        self.btnGrpAcpCanc.addButton(self.btnAceptar)
        self.horizontalLayout2.addWidget(self.btnAceptar)
        self.btnCancelar = QtWidgets.QPushButton(venDialog)
        self.btnCancelar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancelar.sizePolicy().hasHeightForWidth())
        self.btnCancelar.setSizePolicy(sizePolicy)
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnGrpAcpCanc.addButton(self.btnCancelar)
        self.horizontalLayout2.addWidget(self.btnCancelar)
        self.gridLayout.addLayout(self.horizontalLayout2, 1, 0, 1, 1)

        self.retranslateUi(venDialog)
        QtCore.QMetaObject.connectSlotsByName(venDialog)

    def retranslateUi(self, venDialog, msg='', msgAceptar='', msgCancelar=''):
        _translate = QtCore.QCoreApplication.translate
        venDialog.setWindowTitle(_translate("venDialog", "Aviso"))
        self.lblMensajeSalir.setText(_translate("venDialog", msg))
        self.btnAceptar.setText(_translate("venDialog", msgAceptar))
        self.btnCancelar.setText(_translate("venDialog", msgCancelar))
import aviso_rc
