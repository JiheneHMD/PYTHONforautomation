#importe module to interacte with operating system
import os
import datetime

#define local directory where files are located
Directory= r"C:\Users\jihen\Desktop\PYTHONforautomation"
#get the current date and time to later append to new file name structure
Now= datetime.datetime.now()
CurrentDate = Now.strftime("%d-%m-%Y") #function that formats date time into readble
#define a dictionary of old and new file names
ReplacementFilesNames={'file_1.txt':f'file_{CurrentDate}.txt','jihene_2.txt':f'jihene_{CurrentDate}.txt','hello_3.txt':f'hello_{CurrentDate}.txt'}

#loop for iterating renaming
#we can use 'RenamedFiles' as an empty list to keep track of files that we've renamed 
# after loop is complete we join the file rename strings together into a single string with line break

RenamedFiles =[]
for filename in os.listdir(Directory):
    if filename in ReplacementFilesNames.keys():
        Oldname= os.path.join(Directory,filename)
        Newname=os.path.join(Directory,ReplacementFilesNames[filename])
        os.rename(Oldname,Newname)
        RenamedFiles.append(f"{filename}->{ReplacementFilesNames[filename]}")
#print a message indicating renaming of files
print("the following files have being renamed:")
print("\n".join(RenamedFiles))



