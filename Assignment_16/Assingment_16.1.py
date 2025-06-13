import sys

def main():
    filename=sys.argv[1]
    

    fname=open(filename,"a")

    for i in range(2,7):
        fname.write(sys.argv[i])
        fname.write("\n")
        
    


    
if __name__=="__main__":
    main()    