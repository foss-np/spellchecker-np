# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

from Ui_searchwidget import Ui_Form as UI_SearchWidget
from Ui_searchreplacewidget import Ui_Form as UI_SearchReplaceWidget
from Ui_gotolinewidget import Ui_Form as UI_GotoLineWidget

class GotoLineWidget(QtGui.QWidget):
    def __init__(self, editor):
        QtGui.QWidget.__init__(self)
        # Set up the UI from designer
        self.editor=editor
        self.ui=UI_GotoLineWidget()
        self.ui.setupUi(self)
        self.ui.close.clicked.connect(self.hide)
        
    def on_go_clicked(self, b=None):
        if b is not None: return
        cursor=self.editor.textCursor()
        ln=self.ui.line.value()
        block=self.editor.document().findBlockByLineNumber(ln-1)
        pos=block.position()
        cursor.setPosition(pos)
        self.editor.setTextCursor(cursor)
        self.editor.setFocus()
        

class SearchWidget(QtGui.QWidget):
    def __init__(self, editor):
        QtGui.QWidget.__init__(self)
        # Set up the UI from designer
        self.editor=editor
        self.ui=UI_SearchWidget()
        self.ui.setupUi(self)
        self.ui.next.clicked.connect(self.doFind)
        self.ui.previous.clicked.connect(self.doFindBackwards)
        self.ui.close.clicked.connect(self.hide)

    def doFindBackwards (self):
        return self.doFind(backwards=True)

    def doFind(self, backwards=False):
        flags=QtGui.QTextDocument.FindFlags()
        if backwards:
            flags=QtGui.QTextDocument.FindBackward
        if self.ui.matchCase.isChecked():
            flags=flags|QtGui.QTextDocument.FindCaseSensitively

        text=unicode(self.ui.text.text())
        r=self.editor.find(text,flags)

class SearchReplaceWidget(QtGui.QWidget):
    def __init__(self, editor):
        QtGui.QWidget.__init__(self)
        # Set up the UI from designer
        self.ui=UI_SearchReplaceWidget()
        self.ui.setupUi(self)
        self.editor=editor
        self.ui.close.clicked.connect(self.hide)
        self.ui.next.clicked.connect(self.doFindR)
        self.ui.previous.clicked.connect(self.doFindRBackwards)
        self.ui.replace.clicked.connect(self.doReplace)
        self.ui.replaceall.clicked.connect(self.doReplaceAll)

    def doReplaceAllBackwards(self):
        # Backwards and forwards are exactly the
        # same thing if we are replacing all!
        self.doReplaceAll(backwards=True)

    def doReplaceAll(self):
        # Replace all occurences without interaction
        
        old=self.ui.text.text()
        new=self.ui.replaceWith.text()

        # Beginning of undo block
        cursor=self.editor.textCursor()
        cursor.beginEditBlock()
        
        # Use flags for case match
        flags=QtGui.QTextDocument.FindFlags()
        if self.ui.matchCase.isChecked():
            flags=flags|QtGui.QTextDocument.FindCaseSensitively
            
        # Replace all we can
        while True:
            r=self.editor.find(old,flags)
            if r:
                qc=self.editor.textCursor()
                if qc.hasSelection():
                    qc.insertText(new)
            else:
                break
                
        # Mark end of undo block
        cursor.endEditBlock()

    def doReplace(self):
        qc=self.editor.textCursor()
        if qc.hasSelection():
            qc.insertText(self.ui.replaceWith.text())
        self.doFindR(self.backwards)
            
    def doFindRBackwards (self):
        return self.doFindR(backwards=True)

    def doFindR(self, backwards=False):
        self.backwards=backwards
        flags=QtGui.QTextDocument.FindFlags()
        if backwards:
            flags=QtGui.QTextDocument.FindBackward
        if self.ui.matchCase.isChecked():
            flags=flags|QtGui.QTextDocument.FindCaseSensitively

        text=unicode(self.ui.text.text())
        r=self.editor.find(text,flags)
