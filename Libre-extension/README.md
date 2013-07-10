# Libre Extension for Nepali Spellchecker

This _.oxt_ file is an extension that installs Nepali Spell checking in Libre-Office.

---

### How To Install

 - Install Libre. If not preinstalled follow directions from [here](https://www.libreoffice.org/get-help/installation/linux/)
 - Download the _.oxt_ extension
 
```bash
$ wget https://github.com/akshaylb/nepali-spellchecker-v2/raw/master/Libre-extension/ne_NP.oxt
```
 
 - Double click on 'ne_NP.oxt'

### Creating _.oxt_ extensions

_.oxt_ extensions are basically _.zip_ files. 
This extension file is made up of the following files:

 - META-INF
	- manifest.xml
 - description.xml
 - dictionaries.xcu
 - ne_NP.aff
 - ne_NP.dic
 - README_ne_NP.txt
 
To update the extension or modify it, one has to change the _.aff_ and _.dic_ file.
In order to alter this structure for a different language or locale, alterations must be made to all files.

---