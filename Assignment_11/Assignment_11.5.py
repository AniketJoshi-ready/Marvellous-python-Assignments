count=0

def count_zero(num):
    global count
    if num>0:
        digit=num%10   # to get last digit for checking it is zero or not 
        if digit==0:
            count=count+1
        else:
            pass
        num=num//10  # to remove last digit after checking it is 0 or not 
    else:
        return       # for recursion this is must
    count_zero(num) 
    return count    

def main():
    number=int(input("enter the number :  "))
    result=count_zero(number)
    print(result)

if __name__=="__main__":
    main() 