def main():
    num=int(input("enter the number : "))
    fact=1
    while num>1:
        fact=fact*num
        num=num-1

    print("factorial = ",fact)    

if __name__=="__main__":
    main()        