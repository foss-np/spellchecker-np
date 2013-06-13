
all: icons_rc.py Ui_searchreplacewidget.py Ui_searchwidget.py Ui_gotolinewidget.py

icons_rc.py: icons.qrc
	pyrcc4 icons.qrc -o icons_rc.py

Ui_searchreplacewidget.py: searchreplwidget.ui
	pyuic4 searchreplwidget.ui -o Ui_searchreplacewidget.py -x

Ui_searchwidget.py: searchwidget.ui
	pyuic4 searchwidget.ui -o Ui_searchwidget.py -x

Ui_gotolinewidget.py: gotolinewidget.ui
	pyuic4 gotolinewidget.ui -o Ui_gotolinewidget.py -x
