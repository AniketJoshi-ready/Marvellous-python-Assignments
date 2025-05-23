def main():
    size=int(input('enter the size of list numbers : '))
    data=[]
    print("enter the values in list : ")
    for i in range(size):
        ele=int(input())
        data.append(ele)
    print("list of data : ",data)   

    fdata=list(filter(lambda x: x%2==0 ,data))
    print("filtered output : ",fdata)

if __name__=="__main__":
    main()    