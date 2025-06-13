import os

def main():
    filename=input("eneter the text name file : ")
    flag=os.path.exists(filename)

    if flag==True:
        print("file already exist beta samjhe kya ")
    else:
        open(filename,"w")    

    
        


    

if __name__=="__main__":
    main()
