# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gotolinewidget.ui'
#
# Created: Tue Feb 23 22:12:33 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 36)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setMargin(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.close = QtGui.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setAutoRaise(True)
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtGui.QSpinBox(Form)
        self.line.setMinimum(1)
        self.line.setMaximum(99999)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.go = QtGui.QPushButton(Form)
        self.go.setObjectName("go")
        self.horizontalLayout.addWidget(self.go)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label.setBuddy(self.line)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.line, QtCore.SIGNAL("editingFinished()"), self.go.animateClick)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "&Go to line:", None, QtGui.QApplication.UnicodeUTF8))
        self.go.setText(QtGui.QApplication.translate("Form", "G&o", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

