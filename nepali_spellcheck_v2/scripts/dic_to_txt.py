import sys
target=open('ne_NP_wordsonly.txt','w')
target.truncate()
with open('ne_NP_old.dic') as b:
    for data in b:
        i=data.find('/')
        target.write(data[0:i]+'\n')
target.close()
