
import time  
import sys
import os
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
def main():
    s=time.time()
    directory_name=sys.argv[1]

    for foldername,subfoldername,filename in os.walk(directory_name):
        for fname in filename:
            fname=os.path.join(foldername,fname)
            checksum_of_file=calculatechecksum(fname)
            print("checksum of files :",fname,"=",checksum_of_file)
            print()

    duplicate={}

    for FolderName , SubFolderNames, FileNames in os.walk(directory_name):
        for fname in FileNames:
            fname=os.path.join(FolderName,fname)
            checksum=calculatechecksum(fname)

            if checksum in duplicate:
                duplicate[checksum].append(fname)
            else:    
                duplicate[checksum]=[fname]
    print(duplicate)
    Result=list(filter(lambda x: len(x) > 1,duplicate.values()))
    count=0
    for value in Result:
        for subvalue in value:
            count=count+1
            if count > 1 :
                os.remove(subvalue)   
        count=0   
    '''Result=list(filter(lambda x: len(x) > 1,duplicate.values()))

    print()
    print(Result)

    print()
    flog="log.txt"
    flog=open(flog,"a")
    
            
    for f in Result:
        for files in f:
           flog.write(files)
           flog.write("\n")'''


    e=time.time()
    print("execution time : ",e-s)       
          


         

              


if __name__=="__main__":
    main()    
    

    
    





          


         

              


if __name__=="__main__":
    main()   