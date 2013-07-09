# Nepali Spellchecker

A small standalone Nepali Spellchecker based on Hunspell's.

---

### Packages Required

 - [PyQt4][qt4]
 - [pyhunspell][pyhunspell]
 - [regex][regex]

Hunspell to Check Spellings of Nepali unicode.
It is *MANDATORY* for the **'ne_NP.dic'** file and the **'ne_NP.aff'** file to be present inside the hunspell directory.

#### How to Install Packages

###### installing pre-requisite packages
```bash
$ sudo apt-get install python-dev libhunspell ibus-qt pyqt4
```

###### installing pyhunspell
```bash
$ cd path_to_spellchecker/pyhunspell
$ sudo python2 setup.py install
```

###### installing regex
if you have _setuptools_ or _pip_ already installed use:
```bash
$ sudo easy_install-2.7 regex
```
or
```bash
$ sudo pip-2.7 regex
```

### How To Use

After successful installation of prerequisite modules

open the terminal
```bash
$ cd path_to_spellchecker/src
$ python2 main.py
```
===

### FAQ

###### Q. ibus input method not working

 - install `ibus-qt` plugin
 - add `export XMODIFIERS=@im=ibus` to your `.bash.rc` file
 - restart **ibus daemon** with parameters `ibus-daemon --xim -d`

---

If you got any Quetions, post them to [issue][issue] with label **FAQ**

[issue]: https://github.com/akshaylb/nepali-spellchecker-v2/issues/new
[qt4]: http://www.riverbankcomputing.com/software/pyqt/download
[pyhunspell]: https://github.com/akshaylb/nepali-spellchecker-v2/tree/master/pyhunspell
[regex]: https://pypi.python.org/pypi/regex
