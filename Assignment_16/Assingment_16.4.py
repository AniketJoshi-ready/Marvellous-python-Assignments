import sys
def main():
    filename=open("numbers.txt","a")
    for i in range(1,12):
        filename.write(sys.argv[i])
        filename.write("\n")
    filename.close()    
    
        
if __name__=="__main__":
    main()    