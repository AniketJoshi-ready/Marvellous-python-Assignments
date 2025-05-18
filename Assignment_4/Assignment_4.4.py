from functools import reduce
def main():
    size=int(input("enter the size of list of  numbers : "))
    data=[]
    print("enter the numbers/ values : ")
    for i in range(size):
        num=int(input())
        data.append(num)
    print("list of given numbers : ",data)    


    fdata=list(filter( lambda ele: ele%2==0 ,data))
    print("filtered output a even numbers in data  : ",fdata)

    mdata=list(map(lambda ele: ele**2 ,fdata))
    print("mapped data having square of each element  : ",mdata)

    rdata=reduce( lambda x,y: x+y ,mdata)
    print("reduced data with addition  of elements in list : ",rdata)


if __name__=="__main__":
    main()