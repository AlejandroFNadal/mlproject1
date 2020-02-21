#Open file
files=open("training2.csv","r")
if files == None:
    print("Error")
processed=open("ready.csv","w")


#Load all lines to all_lines
all_lines=[]    
all_lines=files.readlines()

#checks if string is still problematic
def check_if_done(line):
    for x in range(0,len(line)-2):
        if line[x] == 'D':
            return False
        elif line[x] =='N':
            return False
        elif line[x] =='S':
            return False
        else:
            if line[x]=='R':
                return False
    return True

while True:
    for line in all_lines:
        print(line)
        new_lines=[]
        for x in range(2,63):
            if line[x] == 'D':
                print("D case")
                new_lines.append(line[0:x]+"A"+line[x+1:len(line)])
                new_lines.append(line[0:x]+"G"+line[x+1:len(line)])
                new_lines.append(line[0:x]+"T"+line[x+1:len(line)])
                all_lines.remove(line)
                break
            elif line[x] =='N':
                print("n case")
                new_lines.append(line[0:x]+"A"+line[x+1:len(line)])
                new_lines.append(line[0:x]+"G"+line[x+1:len(line)])
                new_lines.append(line[0:x]+"T"+line[x+1:len(line)])
                new_lines.append(line[0:x]+"C"+line[x+1:len(line)])
                all_lines.remove(line)
                break
            elif line[x] =='S':
                print("s case")
                new_lines.append(line[0:x]+"C"+line[x+1:len(line)])
                new_lines.append(line[0:x]+"G"+line[x+1:len(line)])
                all_lines.remove(line)
                break
            elif line[x]=='R':
                print("r case")
                new_lines.append(line[0:x]+"A"+line[x+1:len(line)])
                new_lines.append(line[0:x]+"G"+line[x+1:len(line)])
                all_lines.remove(line)
                break
        if new_lines ==[]:
            processed.write(line)
            all_lines.remove(line)
        else:
            inf=0
            sup=len(new_lines)
            z=0
            while new_lines !=[]:
                print("Value z"+str(z))
                print(check_if_done(new_lines[z]))
                if check_if_done(new_lines[z]):
                    if(new_lines[z][len(new_lines[z])-1]== '\n'):
                        processed.write(new_lines[z])
                    else:
                        processed.write(new_lines[z]+'\n')
                    new_lines.pop(z)
                else:
                    all_lines.append(new_lines[z])
                    new_lines.pop(z)
                    #z=z+1
            for l in new_lines:
                print("Length of new lines"+str(len(new_lines)))
                print("check")
                
        ideas+=1
        print(ideas)
        print("size of remaining" +str(len(all_lines)))    
    if all_lines == []:
        break
processed.close()

        
    
        