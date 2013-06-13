# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchreplwidget.ui'
#
# Created: Wed Feb 24 23:59:29 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 72)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(4)
        self.gridLayout.setObjectName("gridLayout")
        self.close = QtGui.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setAutoRaise(True)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 0, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.text = QtGui.QLineEdit(Form)
        self.text.setMinimumSize(QtCore.QSize(200, 0))
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 0, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous = QtGui.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/previous.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous.setIcon(icon1)
        self.previous.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.previous.setAutoRaise(True)
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.previous)
        self.next = QtGui.QToolButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon2)
        self.next.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.next.setAutoRaise(True)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 3, 1, 1)
        self.matchCase = QtGui.QCheckBox(Form)
        self.matchCase.setEnabled(True)
        self.matchCase.setChecked(True)
        self.matchCase.setObjectName("matchCase")
        self.gridLayout.addWidget(self.matchCase, 0, 4, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.replaceWith = QtGui.QLineEdit(Form)
        self.replaceWith.setObjectName("replaceWith")
        self.gridLayout.addWidget(self.replaceWith, 1, 2, 1, 1)
        self.replace = QtGui.QPushButton(Form)
        self.replace.setObjectName("replace")
        self.gridLayout.addWidget(self.replace, 1, 3, 1, 1)
        self.replaceall = QtGui.QPushButton(Form)
        self.replaceall.setObjectName("replaceall")
        self.gridLayout.addWidget(self.replaceall, 1, 4, 1, 1)
        self.label.setBuddy(self.text)
        self.label_2.setBuddy(self.replaceWith)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.text, QtCore.SIGNAL("returnPressed()"), self.next.animateClick)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.text, self.replaceWith)
        Form.setTabOrder(self.replaceWith, self.next)
        Form.setTabOrder(self.next, self.previous)
        Form.setTabOrder(self.previous, self.replace)
        Form.setTabOrder(self.replace, self.replaceall)
        Form.setTabOrder(self.replaceall, self.matchCase)
        Form.setTabOrder(self.matchCase, self.close)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setShortcut(QtGui.QApplication.translate("Form", "Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "&Find:", None, QtGui.QApplication.UnicodeUTF8))
        self.previous.setText(QtGui.QApplication.translate("Form", "&Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.next.setText(QtGui.QApplication.translate("Form", "&Next", None, QtGui.QApplication.UnicodeUTF8))
        self.matchCase.setText(QtGui.QApplication.translate("Form", "&Match Case", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Rep&lace:", None, QtGui.QApplication.UnicodeUTF8))
        self.replace.setText(QtGui.QApplication.translate("Form", "&Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceall.setText(QtGui.QApplication.translate("Form", "Replace &All", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

