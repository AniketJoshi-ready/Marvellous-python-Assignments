from functools import reduce
def chkprime(num):
    label=True
    if num==1 or num==0:
        pass
    else:
        for i in range(2,num):
            if num%i==0:
                label=False
        return label        
    

def main():
    size=int(input("enter the size of list of  numbers : "))
    data=[]
    print("enter the numbers/ values : ")
    for i in range(size):
        num=int(input())
        data.append(num)
    print("list of given numbers : ",data)  

    fdata=list(filter(chkprime,data))
    print("filtered output : ",fdata)

    mdata=list(map(lambda ele: ele*2,fdata))
    print("mapped output : ",mdata)

    rdata=reduce(lambda x,y: x if x>y else y ,mdata)
    print("max no. : ",rdata)




if __name__=="__main__":
    main()


 