from functools import reduce

def main():
    size=int(input("enter the size of list : "))
    data=[]
    print("enter the value : ")
    for i in range(size):
        num=int(input())
        data.append(num)
    print("list of element = ",data)

    fdata=list(filter(lambda x : x%2==0,data)) 
    print("filtered output = ",fdata)

    mdata=list(map(lambda x: x**2 ,fdata))
    print("mapped output = ",mdata)

    rdata=reduce(lambda x,y : x+y ,mdata)
    print("reduced output = ",rdata)   
if __name__=="__main__":
    main()   