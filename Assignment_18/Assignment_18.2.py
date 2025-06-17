def main():
    filename=input("enter the text name : ")
    fname=open(filename,"r")
    content=fname.read()
    print("displaying content of given file : \n",content)

if __name__ == "__main__":
    main()    