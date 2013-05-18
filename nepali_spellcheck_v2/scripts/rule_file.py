import sys
def separate(num): 
    target=open('rule_sets/'+str(num),'w')
    with open('ne_NP_old.txt') as a:
        for line in a:
            if line.find(str(num))!=-1 and line[line.find(str(num))-1]!='1' and line[line.find(str(num))-1]!='2' and line[line.find(str(num))-1]!='3' and line[line.find(str(num))-1]!='4': 
                if (num<10): 
                    if line[line.find(str(num))+1]==',' or line[line.find(str(num))+1]==' ' or line[line.find(str(num))+1]=='\n':
                        target.write(line) 
                if (num>9): 
                    if line[line.find(str(num))+2]==',' or line[line.find(str(num))+2]==' ' or line[line.find(str(num))+2]=='\n':
                        target.write(line)
    target.close()        
    return

for i in range(1,51):
    separate(i)
