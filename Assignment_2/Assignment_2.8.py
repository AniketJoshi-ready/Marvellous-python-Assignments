def main():
    num=int(input("enter the number  : "))
    r=num
    #c=num  it rquire for top down approach
    for i in range(1,r+1):                          # 1,i+1  : this bottom(big) up approach
       for j in range(1,i+1):                       #c-i+1,0,-1  : this is for top(big) down approach
           print(j,end=" ")     # reflect rowise 1234
           #print(i,end=" ")    # reflect columnwise 1234
       print(" ")
       
      
           
           
    
if __name__=="__main__":
    main()