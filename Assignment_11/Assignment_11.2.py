fact=1
def rec_factorial(n):
    global fact
    if n>0:
        fact=fact*n
        n=n-1
    else:
        return  
    
    rec_factorial(n)
    return fact  



def main():
    result=rec_factorial(5)
    print(result)
   
if __name__=="__main__":
    main()   