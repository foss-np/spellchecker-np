# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QMessageBox, QApplication, QMainWindow, QFileDialog
from PyQt4.QtCore import pyqtSlot
from design import Ui_Spellcheck
import codecs
import codecs
from os.path import isfile

class StartQt4(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Spellcheck()
        self.ui.setupUi(self)
        self.watcher=QtCore.QFileSystemWatcher(self)
        QtCore.QObject.connect(self.ui.actionOpen,QtCore.SIGNAL("triggered()"),self.file_open)
        QtCore.QObject.connect(self.ui.actionNew,QtCore.SIGNAL("triggered()"),self.file_new)        
        QtCore.QObject.connect(self.ui.actionSave,QtCore.SIGNAL("triggered()"),self.file_save)
        QtCore.QObject.connect(self.ui.actionClose,QtCore.SIGNAL("triggered()"),self.close)
        QtCore.QObject.connect(self.ui.textEdit,QtCore.SIGNAL("textChanged()"),self.save_enable)
        QtCore.QObject.connect(self.watcher,QtCore.SIGNAL("fileChanged(const QString&)"),self.file_changed)
        self.ui.actionSave.setEnabled(False)
        self.filename=""

    def save_enable(self):
        self.ui.actionSave.setEnabled(True)

    def file_new(self):
        if self.savecheck_dialog():
            return
        self.ui.textEdit.setText('')
        
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
    myapp=StartQt4()
    filename=False
    myapp.show()
    sys.exit(app.exec_())
