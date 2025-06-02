r=1
def power(n,p):
    global r
    if p>0:
        r=r*n
        p=p-1
    else:
        return    
    power(n,p)
    return r  
    
def main():
    num=int(input("enter the number : "))
    power_of_num=int(input("enter the power of number you want : "))

    result=power(num,power_of_num)
    print(result)

if __name__=="__main__":
    main() 