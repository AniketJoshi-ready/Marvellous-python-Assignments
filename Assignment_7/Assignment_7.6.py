def chkprime(num):
    label=True
    if num==0 or num==1:
        pass
    else:
        for i in range(2,num):
            if num%i==0:
                label=False
        return label
            
    
def main():
    data=[]
    size=int(input("size of list : "))
    print("enter the values beta : ")
    for i in range(size):
        ele=int(input())
        data.append(ele)

    print("list of values is : ",data)  



    fdata=list(filter(chkprime,data)) 
    print("filtered output : ",fdata) 


if __name__=="__main__":
    main()    