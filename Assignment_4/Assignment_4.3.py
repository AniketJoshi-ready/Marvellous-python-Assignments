from functools import reduce
def main():
    size=int(input("enter the size of list of  numbers : "))
    data=[]
    print("enter the numbers/ values : ")
    for i in range(size):
        num=int(input())
        data.append(num)
    print("list of given numbers : ",data)    


    fdata=list(filter( lambda ele:70<=ele<=90,data))
    print("filtered output a number greter than or equal to 70 and less than or equal to 90 : ",fdata)

    mdata=list(map(lambda ele: ele+10 ,fdata))
    print("mapped data having each number increased by 10  : ",mdata)

    rdata=reduce( lambda x,y: x*y,mdata)
    print("reduced data return the product of elements in list : ",rdata)


if __name__=="__main__":
    main()
