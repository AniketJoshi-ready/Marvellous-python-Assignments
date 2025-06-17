import sys
import os
import shutil
def main():
    directory_1=sys.argv[1]
    directory_2=sys.argv[2]
    
    os.mkdir(directory_2) # opening our directory 
    

    
    for filename in os.listdir(directory_1):   # we have to read the directory 
            sourcefiles=os.path.join(directory_1,filename)  # joining the path name for that files in directory
            if os.path.isfile(sourcefiles):   # if that file is a file not another directori or subdirectory then goes ahead
             shutil.copy2(sourcefiles,directory_2)
            



            

if __name__=="__main__":
    main()  