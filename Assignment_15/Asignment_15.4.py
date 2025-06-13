import sys
import filecmp
def main():
    file1=sys.argv[1]
    file2=sys.argv[2]

    comparing=filecmp.cmp(file1,file2, shallow=False)   # initailly set false 

    if comparing :
        print("success")
    else:
        print("content NOT SIMILER")    


    

   
    
          
if __name__=="__main__":
    main()    