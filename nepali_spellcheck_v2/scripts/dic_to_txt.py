from sys import argv
script, sourcefile, targetfile = argv
target=open(targetfile,'w')
target.truncate()
with open(sourcefile) as b:
    for data in b:
        i=data.find('/')
        target.write(data[0:i]+'\n')
target.close()
