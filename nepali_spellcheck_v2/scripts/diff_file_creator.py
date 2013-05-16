import sys
target=open('ne_NP.txt','w')
target.truncate()
with open('all_new.txt') as a:
    for line in a:
        with open('ne_NP_wordsonly.txt') as b:
            exists_not=True
            for data in b:
                if data==line:
                    exists_not=False
            if exists_not:
                print 'Writing '+ line
                target.write(line)
target.close()
