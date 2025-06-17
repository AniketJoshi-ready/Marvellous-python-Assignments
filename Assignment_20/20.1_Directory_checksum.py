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
    directory_name=sys.argv[1]

    for foldername,subfoldername,filename in os.walk(directory_name):
        for fname in filename:
            fname=os.path.join(foldername,fname)
            checksum_of_file=calculatechecksum(fname)
            print("checksum of files :",fname,"=",checksum_of_file)


if __name__=="__main__":
    main()    