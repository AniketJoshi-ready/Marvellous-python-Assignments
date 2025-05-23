from functools import reduce

def main():
    size=int(input('enter the size of list numbers : '))
    data=[]
    print("enter the values in list : ")
    for i in range(size):
        ele=int(input())
        data.append(ele)
    print("list of data : ",data) 

    rdata=int(reduce(lambda x,y:x*y , data))  
    print("reduced data : ",rdata)


if __name__=="__main__":
    main()    