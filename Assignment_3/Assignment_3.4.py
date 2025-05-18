def main():
    countnum=int(input("give me count of numbers wanted in list  N :"))
    
    data=list()

    print("enter the  numbers  : ")
    for i in range(countnum):
        num=int(input())
        data.append(num)
    print("list of given number = ",data)

    search_num=int(input("enter the number you want to serch its frquency in given list : "))
    frequency=0
    for i in data :
        if search_num==i:
            frequency=frequency+1

    print("frequency of your searched number : ",frequency)        



if __name__=="__main__":
    main()