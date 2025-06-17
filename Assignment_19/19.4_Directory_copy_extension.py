import os 
import shutil
import sys

def main():
    dir1=sys.argv[1]
    dir2=sys.argv[2]
    extention=sys.argv[3]

    os.mkdir(dir2)

    for filename in os.listdir(dir1):
        files=os.path.join(dir1,filename) # to join path 1st dir name and then filename bhiduu
        if os.path.isfile(files)  and  files.endswith(extention):
            shutil.copy(files,dir2)

if __name__=="__main__":
    main()    