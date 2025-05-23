def main():
    age=int(input("eneter the age : "))
    if age<0 or age>100 :
        print(" chacha this is not valid  age written ")
    else:
        if age>=18:
            print("eligible for vote ")
        else:
            print("not eligible for vote")    
if __name__=="__main__":
    main()        