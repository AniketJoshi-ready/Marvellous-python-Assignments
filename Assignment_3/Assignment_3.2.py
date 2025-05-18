def main():
    countnum=int(input("give me count of numbers wanted in list  N :"))
    
    data=list()

    print("enter the  numbers  : ")
    for i in range(countnum):
        num=int(input())
        data.append(num)
    print("list of given number = ",data)


    max_num=data[0]       # we have to just assume the max number as a first number in list 

    for ele in data:          # iterate that number assumed number in the list and compare it with each element 
        if max_num<ele:       # until new max number not get , when it appear then that number is assumed to be the latest max number and so on we get the maximum number in list
            max_num=ele


    print("maximum number in given lis is : ",max_num)





if __name__=="__main__":
    main()