def chknum(no):
    if no>0:
        print(no," is positive number ")
    elif no<0:
        print(no,"is negative number")
    else:
        print(no,"is zero number")    


def main():
    num=int(input("enter the number : "))
    chknum(num)


if __name__=="__main__":
    main()
    
