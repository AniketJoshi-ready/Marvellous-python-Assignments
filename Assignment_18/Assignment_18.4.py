import sys
def main():
    firstfile=sys.argv[1]
    secondfile=sys.argv[2]

    f1=open(firstfile,"r")
    f2=open(secondfile,"r")

    content_of_f1=f1.read()
    content_of_f2=f2.read()

    if content_of_f1==content_of_f2:
        print("Success")
    else:
        print("Failure")    


if __name__=="__main__":
    main()    