i=1

def pattern(n):
    global i
    if i <=n:
         print("*"*i) 
         i=i+1   
    else:
        return    
    pattern(n)  



def main():
    pattern(5)


if __name__=="__main__":
    main()    