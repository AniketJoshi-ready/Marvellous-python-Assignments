def main():
    a=int(input("eneter first number a : "))
    b=int(input("eneter second number b : "))
    c=int(input("eneter third number c : "))
    if a==b==c:
        print("all are equal ")
    else:    
        if a>b:
            if a>c:
                print(a,"is largest ")
            else:
                print(c,"is largest")
        elif b>a:
            if b>c :
                print(b,"is largest")
            else:
                print(c,"is largest") 
        else:
            print("a&b = ",a, "are equal")
            if a>c:
                print(a,"is largest")
            else:
                print(c,"is largest")    


if __name__=="__main__":
    main()    