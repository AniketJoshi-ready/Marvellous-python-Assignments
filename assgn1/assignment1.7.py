def divby5(no):
    if no % 5== 0 :
        print("True")
    else:
        print("False")

def main():
    num=int(input("enter the number : "))
    print("is it divisible by 5 ? ")
    divby5(num)

if __name__=="__main__":
    main()
    



