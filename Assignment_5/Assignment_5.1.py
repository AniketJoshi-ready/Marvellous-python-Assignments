def sum(x,y):
    return x+y
def difference(x,y):
    return x-y
def multiplication(x,y):
    return x*y

   
    
def main():
    no1=int(input("first number : "))
    no2=int(input("second number : "))
        
        
    s=sum(no1,no2)
    dif=difference(no1,no2)
    m=multiplication(no1,no2)
    print(s)
    print(dif)
    print(m)    
    r=0    
    try:
        r=no1/no2
    except ZeroDivisionError as z:
        print("zero se divide mat karo beta :  ",z)    
        
    print(r)



if __name__=="__main__":
    main()