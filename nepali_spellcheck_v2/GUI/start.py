# -*- coding: utf-8 -*-
import sys
import os
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QMessageBox, QApplication, QMainWindow, QFileDialog
from PyQt4.QtCore import *
from design import Ui_Spellcheck
import codecs
import codecs
from os.path import isfile
import resources

class NepalSCGUI(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Spellcheck()
        self.ui.setupUi(self)

        #Transparency control
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.ui.textEdit.setStyleSheet("background: rgba(0,0,0,20%)")
        #self.ui.toolBar.setStyleSheet("background: rgba(0,0,0,20%)")
        #self.ui.menubar.setStyleSheet("background: rgba(0,0,0,20%)")
        #self.ui.statusbar.setStyleSheet("background: rgba(0,0,0,20%)")
        
        #CSS Importing
        #sshFile="darkorange.stylesheet"
        #with open(sshFile,"r") as fh:
        #   self.setStyleSheet(fh.read())
    
        #actions for toolbar         
        self.newAction = QtGui.QAction(QtGui.QIcon('Resources/New.png'), 'New', self)
        self.openAction = QtGui.QAction(QtGui.QIcon('Resources/Open.png'), 'Open', self)
        self.saveAction = QtGui.QAction(QtGui.QIcon('Resources/Save.png'), 'Save', self)
        self.cutAction = QtGui.QAction(QtGui.QIcon('Resources/Cut.png'), 'Cut', self)
        self.copyAction = QtGui.QAction(QtGui.QIcon('Resources/Copy.png'), 'Copy', self)
        self.pasteAction = QtGui.QAction(QtGui.QIcon('Resources/Paste.png'), 'Paste', self)
        self.closeAction = QtGui.QAction(QtGui.QIcon('Resources/Close.png'), 'Close', self)

        #toolbar sequencing
        self.ui.menubar.setContextMenuPolicy(Qt.NoContextMenu)
        self.ui.toolBar.setContextMenuPolicy(Qt.NoContextMenu)
        self.ui.toolBar.setIconSize(QSize(16,16))
        self.ui.toolBar.addAction(self.newAction)
        self.ui.toolBar.addAction(self.openAction)
        self.ui.toolBar.addAction(self.saveAction)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addAction(self.cutAction)
        self.ui.toolBar.addAction(self.copyAction)
        self.ui.toolBar.addAction(self.pasteAction)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addAction(self.closeAction)
        
        #slots
        self.watcher=QtCore.QFileSystemWatcher(self)
        self.newAction.triggered.connect(self.file_new)
        self.openAction.triggered.connect(self.file_open)
        self.saveAction.triggered.connect(self.file_save)
        self.cutAction.triggered.connect(self.ui.textEdit.cut)
        self.copyAction.triggered.connect(self.ui.textEdit.copy)
        self.pasteAction.triggered.connect(self.ui.textEdit.paste)
        self.closeAction.triggered.connect(self.close)
        self.ui.actionClose.triggered.connect(self.close)        
        self.ui.actionOpen.triggered.connect(self.file_open)
        self.ui.actionNew.triggered.connect(self.file_new)
        self.ui.actionSave.triggered.connect(self.file_save)
        self.ui.textEdit.textChanged.connect(self.save_enable)
        self.ui.actionCut.triggered.connect(self.ui.textEdit.cut)
        self.ui.actionCopy.triggered.connect(self.ui.textEdit.copy)
        self.ui.actionPaste.triggered.connect(self.ui.textEdit.paste)	
        self.watcher.fileChanged.connect(self.file_changed)
        self.ui.actionSave.setEnabled(False)
        self.filename=""

    def save_enable(self):
        self.ui.actionSave.setEnabled(True)
        if self.filename:
            self.setWindowTitle(unicode(self.objectName()+" - " + self.filename + "[*]") )

    def file_new(self):
        if self.savecheck_dialog():
            return
        self.ui.textEdit.setText('')
        self.ui.actionSave.setEnabled(False)
        
    def file_open(self):
        if self.savecheck_dialog():
            return
        self.filename=QtGui.QFileDialog.getOpenFileName(self, "Open file", ".")
        from os.path import isfile
        if isfile(self.filename):
            if self.filename:
                self.watcher.removePath(self.filename)
            import codecs
            text=codecs.open(self.filename,'r','utf-8').read()
            self.ui.textEdit.setPlainText(text)
            self.ui.actionSave.setEnabled(False)
            self.watcher.addPath(self.filename)
            self.setWindowTitle(unicode(self.objectName()+" - " + self.filename) )
    
    def file_changed(self,path):
        res=QMessageBox.question(self, "%s - File has been changed" %self.objectName(),"The opened document has been modified by another program.\n"+"Do you want to reload the file?",QMessageBox.Yes|QMessageBox.No|(QMessageBox.Save if self.button.actionSave.isEnabled() else 0),QMessageBox.Yes)
        if res == QMessageBox.Yes:
            self.file_open(self.filename)
        elif res == QMessageBox.Save:
            self.file_save()
            
    def file_save(self):
        from os.path import isfile
        self.watcher.removePath(self.filename)
        if not isfile(self.filename):
            self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.txt')
        import codecs
        savetext=codecs.open(self.filename,'w','utf-8')
        savetext.write(unicode(self.ui.textEdit.toPlainText()))
        savetext.close()
        self.ui.actionSave.setEnabled(False)
        self.watcher.addPath(self.filename)

    def savecheck_dialog(self):    
        if not self.ui.actionSave.isEnabled():
            return  
        res=QMessageBox.question(self, "%s - Unsaved Changes"% self.objectName(),"The document has been modified\n"+"Do you want to save your changes?", QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
        print(res)
        if res==QMessageBox.Save:
            self.file_save()
        return res==QMessageBox.Cancel
        
    def closeEvent(self,event):
        if self.savecheck_dialog():
            event.ignore()
        else:
            event.accept()
        
if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=NepalSCGUI()
    filename=False
    myapp.show()
    sys.exit(app.exec_())
