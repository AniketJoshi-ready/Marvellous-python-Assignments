import os
import sys
import time
import hashlib
def calculatechecksum(path,blocksize=1024):
    fobj=open(path,"rb")

    hobj=hashlib.md5()

    buffer=fobj.read(blocksize)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer=fobj.read(blocksize)
    fobj.close()

    return hobj.hexdigest()    


def DirectoryWatcher(DirectoryName = "Demo"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
        
    

    

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=calculatechecksum(fname)
            print("filename :  ",fname)
            print("checksum : ",checksum)
            print()

    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    fobj = open(filename,"w")

    Border = "-"*54
    
    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script\n")
    fobj.write("This is a Driectory Cleaner Script\n")

    fobj.write(Border+"\n")

    

    fobj.write("\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("This is is created at \n"+timestamp+"\n")
    fobj.write(Border+"\n")


def FindDuplicate(DirectoryName = "marvellous"):

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
        
    

    
    duplicate={}

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=calculatechecksum(fname)

            if checksum in duplicate:
                duplicate[checksum].append(fname)
            else:    
                duplicate[checksum]=[fname]
    return duplicate       
def displayresult(MyDict):
    Result=list(filter(lambda x: len(x) > 1,MyDict.values()))
    
    count=0
    for value in Result:
        for subvalue in value:
            count=count+1
            print(subvalue)
        print("---------------------------------------------")  
        print("value of count : ",count)
        print("---------------------------------------------")    
        count=0


def deleteduplicate(MyDict):
    Result=list(filter(lambda x: len(x) > 1,MyDict.values()))
    foldername="marvellous"      # logbook folder
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    filename=os.path.join(foldername,"marvellog.txt")   # log text
    fname=open(filename,"a")
    count=0
    for value in Result:
        for subvalue in value:
            count=count+1
            if count > 1 :
                fname.write("%s \n"%subvalue)  # before delete it should be written in log
                os.remove(subvalue)   
        count=0        

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")

        else:
            result=FindDuplicate(sys.argv[1])
            deleteduplicate(result)

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

if __name__ == "__main__":
    main()