from sys import argv
script, sourcefile, compfile, targetfile = argv
target=open(targetfile,'w')
target.truncate()
with open(sourcefile) as a:
    for line in a:
        with open(compfile) as b:
            exists_not=True
            for data in b:
                if data==line:
                    exists_not=False
            if exists_not:
                print 'Writing '+ line
                target.write(line)
target.close()
