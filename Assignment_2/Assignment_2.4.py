def main():
    num=int(input("enter number  : "))
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    
    
    print("addition of numbers which divides given number completely : ",sum)        
        

       
      
           
           
       

        
        
        
          

if __name__=="__main__":
    main()