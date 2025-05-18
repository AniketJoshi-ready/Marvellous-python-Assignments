def main():
    num=int(input("enter the number : "))
    temp=num
    counter=0
    
    while temp>0:
        temp=temp//10   # we get quotiont so we remove the unit place in each iteration 
        counter=counter+1
    print("count the digit in number : ",counter)    

         
if __name__=="__main__":
    main()    