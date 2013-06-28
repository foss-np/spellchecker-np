# Nepali Spellchecker

A small standalone Nepali Spellchecker based on hunspell.

---

### Packages Required

 - [PyQt4][qt4]
 - [pyhunspell][pyhunspell]
 - [regex][regex]

Hunspell to Check Spellings of Nepali unicode.
It is *MANDATORY* for the **'ne_NP.dic'** file and the **'ne_NP.aff'** file to be present inside the hunspell directory.

#### How to Install Packages

######installing pre-requisite packages
```bash
$ sudo apt-get install python-dev libhunspell ibus-qt pyqt4
```

######installing pyhunspell
```bash
$ cd path_to_spellchecker/pyhunspell
$ sudo python setup.py install
```

######installing regex
if you have _setuptools_ or _pip_ already installed use:
```bash
$ easy_install regex
```
or
```bash
$ pip regex
```

else follow the following steps:

1. download the tar from [here][regexpypi]
2. cd into download directory
3. type in the following

```bash
$ tar -zxvf regex-2013-06-26.tar.gz
$ cd regex-2013-06-26
$ sudo python setup.py install
```

###How To Use

After successful installation of prerequisite modules

open the terminal
```bash
$ cd path_to_spellchecker/src
$ python2 main.py
```

### FAQ

Please post it into [issue][issue] with label ***FAQ***

[issue]: https://github.com/akshaylb/nepali-spellchecker-v2/issues/new
[qt4]: http://www.riverbankcomputing.com/software/pyqt/download
[pyhunspell]: https://github.com/akshaylb/nepali-spellchecker-v2/tree/master/pyhunspell
[regex]: https://pypi.python.org/pypi/regex
[regexpypi]: https://pypi.python.org/packages/source/r/regex/regex-2013-06-26.tar.gz
