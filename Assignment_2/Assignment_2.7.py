def main():
    num=int(input("enter the number  : "))
    for i in range(1,num+1):
       for j in range(1,num+1):
           print(j,end=" ")     # reflect rowise 1234
           #print(i,end=" ")    # reflect columnwise 1234
       print(" ")
       
      
           
           
    
if __name__=="__main__":
    main()