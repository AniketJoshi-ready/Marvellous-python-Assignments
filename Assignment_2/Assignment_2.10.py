def main():
    num=int(input("enter the number : "))
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit
        temp=temp//10   # if we want the tenth and upper place digit in number we go towords quotiont for we need FLOOR DIVISION OPERATOR //
    print("sum of digits in given number :  ",sum)
   

if __name__=="__main__":
    main()   