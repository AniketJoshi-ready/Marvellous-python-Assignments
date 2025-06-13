import shutil
import sys

def main():
   # firstfile=input("enter the name of existing file :first file :  ")   GARAJ NAHI
   firstfile=sys.argv[1]
   secondfile=sys.argv[2]

   #fname=open(firstfile,"r") GARAJ NAHI 
    
    #secondfile=input("eneter the new file name :second file :") GARAJ NAHI
   cpy=shutil.copyfile(firstfile,secondfile)
   # print(cpy)    GARAJ NAHI

    



if __name__=="__main__":
    main()    