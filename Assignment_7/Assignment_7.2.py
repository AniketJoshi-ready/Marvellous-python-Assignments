def main():
    size=int(input('enter the size of list numbers : '))
    data=[]
    print("enter the values in list : ")
    for i in range(size):
        ele=int(input())
        data.append(ele)
    print("list of data : ",data)   

    mdata=list(map(lambda x: x*2, data)) 
    print("mapped output : ",mdata)


if __name__=="__main__":
    main()