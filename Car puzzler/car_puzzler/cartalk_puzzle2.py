def read_file():
    fin=open("words.txt","r")
    for line in fin:
        word=line.strip().split()
        key=word[0]
        pron=' '.join(word[1:])
        dic[key]=pron
    fin.close()
    
  
#the program execution starts form here
dic={} # or dict()

#calling method
read_file()

max_level=0

#here is the logic to solve puzzle
print "KEY\t\tENGLISH WORDS\t\tMAXIMUM WORDS"
print "-------------------------------------------------------"
for key,value in  dic.items():
     temp_list=[]
     #remove first letter from key and add it to temporarty list
     for i in range(1,len(key)):
                    temp_list.append(key[i:])
                    
     count=0 
     if len(temp_list)>max_level:
         for element in temp_list:
             if element not in dic:
                 break
             count=count+1
             
         #if any other elements has more words than it's prev override max_level            
         if count>max_level:
             max_level=count
             print key,"==>",temp_list,":",max_level

print "FINISHED!"
                
        

