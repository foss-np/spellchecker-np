# -*- coding: utf-8 -*-
import sys
import os
from PyQt4.Qt import QSyntaxHighlighter, QAction, QTextCharFormat, QTextCursor, QMenu, QMouseEvent, QTextEdit
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QMessageBox, QApplication, QMainWindow, QFileDialog
from PyQt4.QtCore import *
from design import Ui_Spellcheck
import codecs
import codecs
from os.path import isfile
import resources
import webbrowser
import hunspell
import regex


class NepalSCGUI(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Spellcheck()
        self.ui.setupUi(self)
        self.hidewidgets()
        self.checker=hunspell.HunSpell('hunspell/ne_NP.dic','hunspell/ne_NP.aff')
        self.highlighter = Highlighter(self.ui.textEdit.document())
        self.highlighter.setDict(self.checker)
        self.ui.toolBar.setContextMenuPolicy(Qt.NoContextMenu)
        self.ui.formatBar.setContextMenuPolicy(Qt.NoContextMenu)
        self.ui.textEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.textEdit.customContextMenuRequested.connect(self.showContextMenu)
        self.ui.textEdit.mousePressedSignal.connect(self.OnMousePressed)
        self.ui.textEdit.setAttribute(QtCore.Qt.WA_InputMethodEnabled, True) 
        
        for i in range(1,3):
            self.ui.textEdit.zoomIn()
        #self.importCSS('DarkOrange/darkorange.stylesheet')
        #self.importCSS('qdarkstyle/style.qss')
        #Define actions for toolbar         
        self.mppAction = QtGui.QAction(QtGui.QIcon('Resources/mpplogo.gif'), 'Madan Puraskar Pustakalaya', self)
        self.newAction = QtGui.QAction(QtGui.QIcon('Resources/New.png'), 'New', self)
        self.openAction = QtGui.QAction(QtGui.QIcon('Resources/Open.png'), 'Open', self)
        self.saveAction = QtGui.QAction(QtGui.QIcon('Resources/Save.png'), 'Save', self)
        self.saveAsAction = QtGui.QAction(QtGui.QIcon('Resources/SaveAs.png'), 'SaveAs', self)
        self.cutAction = QtGui.QAction(QtGui.QIcon('Resources/Cut.png'), 'Cut', self)
        self.copyAction = QtGui.QAction(QtGui.QIcon('Resources/Copy.png'), 'Copy', self)
        self.pasteAction = QtGui.QAction(QtGui.QIcon('Resources/Paste.png'), 'Paste', self)
        self.closeAction = QtGui.QAction(QtGui.QIcon('Resources/Close.png'), 'Close', self)
        #Define Buttons
        self.bold_button = QtGui.QToolButton(self)
        self.defineButton(self.bold_button,'Resources/format-text-bold.png',True,True,'Ctrl+B','Bold',self.set_bold)
        self.italic_button = QtGui.QToolButton(self)
        self.defineButton(self.italic_button,'Resources/format-text-italic.png',True,True,'Ctrl+I','Italic',self.set_italic)
        self.underline_button = QtGui.QToolButton(self)
        self.defineButton(self.underline_button,'Resources/format-text-underline.png',True,True,'Ctrl+U','Underline',self.set_underline)
        self.alignleft_button = QtGui.QToolButton(self)
        self.defineButton(self.alignleft_button,'Resources/format-justify-left.png',True,True,'Ctrl+L','Align Left',self.set_alignleft)
        self.aligncenter_button = QtGui.QToolButton(self)
        self.defineButton(self.aligncenter_button,'Resources/format-justify-center.png',True,True,'Ctrl+E','Align Center',self.set_aligncenter)
        self.alignright_button = QtGui.QToolButton(self)
        self.defineButton(self.alignright_button,'Resources/format-justify-right.png',True,True,'Ctrl+R','Align Right',self.set_alignright)
        self.zoomin_button = QtGui.QToolButton(self)
        self.defineButton(self.zoomin_button,'Resources/list-add.png',True,False,'Ctrl++','Zoom In',self.ui.textEdit.zoomIn)
        self.zoomout_button = QtGui.QToolButton(self)
        self.defineButton(self.zoomout_button,'Resources/list-remove.png',True,False,'Ctrl+-','Zoom Out',self.ui.textEdit.zoomOut)
        self.color_button = QtGui.QToolButton(self)
        self.defineButton(self.color_button,'Resources/color.png',True,False,None,'Color',self.set_color)
        #toolbar sequencing
        self.ui.menubar.setContextMenuPolicy(Qt.NoContextMenu)
        self.ui.toolBar.setContextMenuPolicy(Qt.NoContextMenu)
        self.ui.toolBar.setIconSize(QSize(22,22))
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addAction(self.newAction)
        self.ui.toolBar.addAction(self.openAction)
        self.ui.toolBar.addAction(self.saveAction)
        self.ui.toolBar.addAction(self.saveAsAction)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addAction(self.closeAction)
        #formatbar sequencing
        self.ui.formatBar.setIconSize(QSize(22,22))
        self.ui.formatBar.addAction(self.mppAction)
        self.ui.formatBar.addSeparator()
        self.ui.formatBar.addAction(self.cutAction)
        self.ui.formatBar.addAction(self.copyAction)
        self.ui.formatBar.addAction(self.pasteAction)
        self.ui.formatBar.addSeparator()
        self.ui.formatBar.addWidget(self.bold_button)
        self.ui.formatBar.addWidget(self.italic_button)
        self.ui.formatBar.addWidget(self.underline_button)
        self.ui.formatBar.addSeparator()
        self.ui.formatBar.addWidget(self.alignleft_button)
        self.ui.formatBar.addWidget(self.aligncenter_button)
        self.ui.formatBar.addWidget(self.alignright_button)
        self.ui.formatBar.addSeparator()
        self.ui.formatBar.addWidget(self.color_button)
        self.ui.formatBar.addSeparator()
        self.ui.formatBar.addWidget(self.zoomin_button)
        self.ui.formatBar.addWidget(self.zoomout_button)
        #slots
        self.watcher=QtCore.QFileSystemWatcher(self)
        self.newAction.triggered.connect(self.file_new)
        self.openAction.triggered.connect(self.file_open)
        self.saveAction.triggered.connect(self.file_save)
        self.saveAsAction.triggered.connect(self.file_saveAs)
        self.cutAction.triggered.connect(self.ui.textEdit.cut)
        self.copyAction.triggered.connect(self.ui.textEdit.copy)
        self.pasteAction.triggered.connect(self.ui.textEdit.paste)
        self.closeAction.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionClose.triggered.connect(self.close)        
        self.ui.actionOpen.triggered.connect(self.file_open)
        self.ui.actionNew.triggered.connect(self.file_new)
        self.ui.actionSave.triggered.connect(self.file_save)
        self.ui.textEdit.textChanged.connect(self.save_enable)
        self.ui.actionCut.triggered.connect(self.ui.textEdit.cut)
        self.ui.actionCopy.triggered.connect(self.ui.textEdit.copy)
        self.ui.actionPaste.triggered.connect(self.ui.textEdit.paste)
        self.ui.actionUndo.triggered.connect(self.ui.textEdit.undo)
        self.ui.actionRedo.triggered.connect(self.ui.textEdit.redo)
        self.ui.actionGoto.triggered.connect(self.gotoline)
        self.ui.actionSearch.triggered.connect(self.find)
        self.ui.actionReplace.triggered.connect(self.replace)
        self.watcher.fileChanged.connect(self.file_changed)
        self.mppAction.triggered.connect(self.open_mpp)
        self.EscAction = QtGui.QShortcut(QtGui.QKeySequence(self.tr("Esc")), self);
        self.EscAction.activated.connect(self.hidewidgets)
        self.ui.actionSave.setEnabled(False)
        self.saveAction.setEnabled(False)
        self.filename=""
        #self.ui.textEdit.setStyleSheet("QTextEdit {color:white}")
        self.update_text()
    #Imports CSS stylesheet to the QMainWindow    
    def importCSS(self, path):
        sshFile="stylesheets/"+path
        with open(sshFile,"r") as fh:
           self.setStyleSheet(fh.read())
    #Links to MPP website
    def open_mpp(self):
        webbrowser.open('http://madanpuraskar.org/')
    #Hides extra widgets
    def hidewidgets(self):
        self.ui.Gotowidget.hide()
        self.ui.Findwidget.hide()
        self.ui.Replacewidget.hide()
        self.ui.textEdit.setFocus()
    #Defines Button Actions
    def defineButton(self,button, Icon, Raise, Check, Shortcut, Tooltip, Action):
        button.setIcon(QtGui.QIcon(Icon))
        button.setAutoRaise(Raise)
        button.setCheckable(Check)
        button.setShortcut(QtGui.QKeySequence(Shortcut))
        button.setToolTip(Tooltip)
        button.clicked.connect(Action)
        return button
    #Enables Save feature
    def save_enable(self):
        self.ui.actionSave.setEnabled(True)
        self.saveAction.setEnabled(True)
        if self.filename:
            self.setWindowTitle(unicode(self.objectName()+" - " + self.filename + "[*]") )
    #Creates new file
    def file_new(self):
        if self.savecheck_dialog():
            return
        self.ui.textEdit.setText('')
        self.ui.actionSave.setEnabled(False)
        self.saveAction.setEnabled(False)
    #Opens existing File
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
            self.saveAction.setEnabled(False)
            self.watcher.addPath(self.filename)
            self.setWindowTitle(unicode(self.objectName()+" - " + self.filename) )
    #Checks if file has been changed
    def file_changed(self,path):
        res=QMessageBox.question(self, "%s - File has been changed" %self.objectName(),"The opened document has been modified by another program.\n"+"Do you want to reload the file?",QMessageBox.Yes|QMessageBox.No|(QMessageBox.Save if self.button.actionSave.isEnabled() else 0),QMessageBox.Yes)
        if res == QMessageBox.Yes:
            self.file_open(self.filename)
        elif res == QMessageBox.Save:
            self.file_save()
    #AboutBox
    def about(self):
        res=QMessageBox.about(self, "%s - About" %self.objectName(),"Nepali Spellchecker v2 is a small software created by Language and Technology Kendra (LTK) a division of Madan Puraskar Pustakalaya.\n"+"All rights reserved.")
        if res == QMessageBox.Ok:
            return
    #Saves file
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
        self.saveAction.setEnabled(False)
        self.watcher.addPath(self.filename)
    #SaveAs feature
    def file_saveAs(self):
        from os.path import isfile
        self.watcher.removePath(self.filename)
        self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.txt')
        import codecs
        savetext=codecs.open(self.filename,'w','utf-8')
        savetext.write(unicode(self.ui.textEdit.toPlainText()))
        savetext.close()
        self.ui.actionSave.setEnabled(False)
        self.saveAction.setEnabled(False)
        self.watcher.addPath(self.filename)
    #Dialog Box before closing
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
    
    def set_bold(self):
        if self.bold_button.isChecked():
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setFontWeight(QtGui.QFont.Bold)
        else:
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setFontWeight(QtGui.QFont.Normal)

    def set_italic(self, bool):
        if bool:
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setFontItalic(True)
        else:
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setFontItalic(False)

    def set_underline(self, bool):
        if bool:
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setFontUnderline(True)
        else:
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setFontUnderline(False)
            
    def set_alignleft(self, bool):
        if bool:
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setAlignment(Qt.AlignLeft)
        self.update_alignment(Qt.AlignLeft)

    def set_aligncenter(self, bool):
        if bool:
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setAlignment(Qt.AlignCenter)
        self.update_alignment(Qt.AlignCenter)

    def set_alignright(self, bool):
        if bool:
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setAlignment(Qt.AlignRight)
        self.update_alignment(Qt.AlignRight)

    def update_alignment(self, al=None):
        if al is None:
            al = self.ui.textEdit.alignment()
        if al == Qt.AlignLeft:
            self.alignleft_button.setChecked(True)
            self.aligncenter_button.setChecked(False)
            self.alignright_button.setChecked(False)
        elif al == Qt.AlignCenter:
            self.aligncenter_button.setChecked(True)
            self.alignleft_button.setChecked(False)
            self.alignright_button.setChecked(False)
        elif al == Qt.AlignRight:
            self.alignright_button.setChecked(True)
            self.alignleft_button.setChecked(False)
            self.aligncenter_button.setChecked(False)

    def set_color(self):
        color = QtGui.QColorDialog.getColor(self.ui.textEdit.textColor())
        if color.isValid():
            self.ui.textEdit.setFocus(Qt.OtherFocusReason)
            self.ui.textEdit.setTextColor(color)
            pixmap = QtGui.QPixmap(16, 16)
            pixmap.fill(color)
            self.color_button.setIcon(QtGui.QIcon(pixmap))

    def update_color(self):
        color = self.ui.textEdit.textColor()
        pixmap = QtGui.QPixmap(16, 16)
        pixmap.fill(color)
        self.color_button.setIcon(QtGui.QIcon(pixmap))

    def update_format(self, format):
        font = format.font()
        self.bold_button.setChecked(font.bold())
        self.italic_button.setChecked(font.italic())
        self.underline_button.setChecked(font.underline())
        self.update_alignment(self.ui.textEdit.alignment())

    def update_text(self):
        self.update_alignment()
        self.update_color()
    #Function for Goto widget
    def gotoline(self):
        self.ui.Gotowidget.show()
        self.ui.lineNo.setFocus()
        self.ui.lineNo.returnPressed.connect(self.gotoaction)
        self.ui.GoButton.clicked.connect(self.gotoaction)
       
    def gotoaction(self):
        ln=int(self.ui.lineNo.text())
        self.ui.Gotowidget.hide()
        if (ln==None): return
        cursor=self.ui.textEdit.textCursor()
        block=self.ui.textEdit.document().findBlockByLineNumber(ln)
        pos=block.position()
        cursor.setPosition(pos)
        self.ui.textEdit.setTextCursor(cursor)
        self.ui.textEdit.setFocus()        
    #Function for Find Widget
    def find(self):
        if self.ui.Replacewidget.isVisible():
            self.ui.Replacewidget.hide()
        self.ui.Findwidget.show()
        self.ui.SearchKey.setFocus()
        self.ui.SearchKey.returnPressed.connect(self.doFind)
        self.ui.next.clicked.connect(self.doFind)
        self.ui.previous.clicked.connect(self.doFindBackwards)

    def doFindBackwards (self):
        return self.doFind(backwards=True)

    def doFind(self, backwards=False):
        rotationIncomplete=True
        flags=QtGui.QTextDocument.FindFlags()
        if backwards:
            flags=QtGui.QTextDocument.FindBackward
        if self.ui.MatchCase.isChecked():
            flags=flags|QtGui.QTextDocument.FindCaseSensitively
        if self.ui.Findwidget.isVisible():
            text=unicode(self.ui.SearchKey.text())
        elif self.ui.Replacewidget.isVisible():
            text=unicode(self.ui.OldText.text())
        r=self.ui.textEdit.find(text,flags)
        if r==False:
            if rotationIncomplete:
                self.ui.textEdit.moveCursor(QtGui.QTextCursor.Start)
                rotationIncomplete=False
            else:
                QMessageBox.information(self, "End of Search", "No more occurences of the word can be found.")
    #Funtion for Replace widget
    def replace(self):
        if self.ui.Findwidget.isVisible():
            self.ui.Findwidget.hide()
        self.ui.Replacewidget.show()
        self.ui.OldText.setFocus()
        self.ui.OldText.returnPressed.connect(self.doFind)
        self.ui.next_2.clicked.connect(self.doFind)
        self.ui.previous_2.clicked.connect(self.doFindBackwards)
        self.ui.replace.clicked.connect(self.doReplace)
        self.ui.r_all.clicked.connect(self.doReplaceAll)

    def doReplace(self, backwards=False):
        cursor=self.ui.textEdit.textCursor()
        if cursor.hasSelection():
            cursor.insertText(self.ui.NewText.text())
        else:
            flags=QtGui.QTextDocument.FindFlags()
            if backwards:
                flags=QtGui.QTextDocument.FindBackward
            if self.ui.MatchCase_2.isChecked():
                flags=flags|QtGui.QTextDocument.FindCaseSensitively
            text=unicode(self.ui.OldText.text())
            r=self.ui.textEdit.find(text,flags)
            if cursor.hasSelection():
                cursor.insertText(self.ui.NewText.text())
            if r==False:
                QMessageBox.information(self, "End of Search", "No more occurences of the word can be found.")
        
    def doReplaceAll(self):
        cursor=self.ui.textEdit.textCursor()
        cursor.beginEditBlock()
        flags=QtGui.QTextDocument.FindFlags()
        if self.ui.MatchCase_2.isChecked():
            flags=flags|QtGui.QTextDocument.FindCaseSensitively
        text=unicode(self.ui.OldText.text())
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.Start)
        while True:
            r=self.ui.textEdit.find(text,flags)
            if r:
                qc=self.ui.textEdit.textCursor()
                if qc.hasSelection():
                    qc.insertText(self.ui.NewText.text())
            else:
                QMessageBox.information(self, "End of Search", "All occurences replaced.")    
                break
        cursor.endEditBlock()
    #Mouse Press Event for QTextEdit
    def OnMousePressed(self, position):
        cursor = self.ui.textEdit.cursorForPosition(position)
        self.ui.textEdit.setTextCursor(cursor)
    #ContextMenu creator for QtextEdit
    def showContextMenu(self, position):
        SuggestionContextMenu = self.ui.textEdit.createStandardContextMenu()
        cursor=self.ui.textEdit.textCursor()
        cursor.select(QTextCursor.WordUnderCursor)
        self.ui.textEdit.setTextCursor(cursor)
        if self.ui.textEdit.textCursor().hasSelection():
            a=self.ui.textEdit.textCursor().selectedText()
            if a[-1]==u'।':
                a=a.remove(u'।')
                cursor.movePosition(QTextCursor.Left,QTextCursor.KeepAnchor)
                self.ui.textEdit.setTextCursor(cursor)
            text = unicode(a).encode('utf-8')
            if not self.checker.spell(text):
                ignoreAction=QAction('Ignore',SuggestionContextMenu)
                ignoreAction.triggered.connect(self.ignoreSelection)
                addAction=QAction('Add to Dictionary',SuggestionContextMenu)
                addAction.triggered.connect(self.addWord)
                SuggestionContextMenu.insertSeparator(SuggestionContextMenu.actions()[0])
                SuggestionContextMenu.insertAction(SuggestionContextMenu.actions()[0], addAction)
                SuggestionContextMenu.insertAction(SuggestionContextMenu.actions()[0], ignoreAction)
                SuggestionMenu = QMenu('Spelling Suggestions')
                for word in self.checker.suggest(text):
                    word=word.decode('utf-8')
                    action = SuggestAction(word, SuggestionMenu)
                    action.correct.connect(self.replaceCorrect)
                    SuggestionMenu.addAction(action)
                if len(SuggestionMenu.actions()) != 0:
                   SuggestionContextMenu.insertMenu(SuggestionContextMenu.actions()[0], SuggestionMenu)
        cursor.clearSelection()
        SuggestionContextMenu.exec_(self.ui.textEdit.mapToGlobal(position))
        self.ui.textEdit.setTextCursor(cursor)
    #Function for ignore function
    def ignoreSelection(self):
        a=self.ui.textEdit.textCursor().selectedText()
        if a[-1]==u'।':
            a=a.remove(u'।')
            cursor.movePosition(QTextCursor.Left,QTextCursor.KeepAnchor)
            self.ui.textEdit.setTextCursor(cursor)
        text = unicode(a).encode('utf-8')
        self.checker.add(text)
    #Function for SPell Corrector        
    def replaceCorrect(self, word):
        cursor = self.ui.textEdit.textCursor()
        cursor.beginEditBlock()
        cursor.removeSelectedText()
        cursor.insertText(word)
        cursor.endEditBlock()
    #aAdd new words to dic file
    def addWord(self):
        a=self.ui.textEdit.textCursor().selectedText()
        if a[-1]==u'।':
            a=a.remove(u'।')
            cursor.movePosition(QTextCursor.Left,QTextCursor.KeepAnchor)
            self.ui.textEdit.setTextCursor(cursor)
        text = unicode(a)
        dictionary = codecs.open('hunspell/ne_NP.dic','r','utf-8').read()
        words=dictionary.split('\n')
        words.append(text)
        words[0]=unicode(len(words)-2)
        dictionary = codecs.open('hunspell/ne_NP.dic','w','utf-8')
        dictionary.write(u'\n'.join(words))
        dictionary.close()
        self.checker=hunspell.HunSpell('hunspell/ne_NP.dic','hunspell/ne_NP.aff')
        self.highlighter.setDict(self.checker)
#QAction class for all suggestion menus
class SuggestAction(QAction):
    correct = pyqtSignal(unicode)
    def __init__(self, *args):
        QAction.__init__(self, *args)
        self.triggered.connect(lambda x: self.correct.emit(self.text()))
#Highlighter class underlines incorrect words
class Highlighter(QSyntaxHighlighter):
    pattern = ur'(?u)\w+' 

    def __init__(self, *args):
        QSyntaxHighlighter.__init__(self, *args)
        self.dict = None
        
    def setDict(self, dict):
        self.dict = dict
        
    def highlightBlock(self, text):
        if not self.dict:
            return
        if not text:
            return
        text = unicode(text)
        format = QTextCharFormat()
        format.setUnderlineColor(Qt.red)
        format.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
        unicode_pattern=regex.compile(self.pattern,regex.UNICODE)
        for word_object in unicode_pattern.finditer(text):
            if not self.dict.spell(word_object.group().encode('utf-8')):
                self.setFormat(word_object.start(), word_object.end() - word_object.start(), format)

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp=NepalSCGUI()
    filename=False
    myapp.show()
    sys.exit(app.exec_())
