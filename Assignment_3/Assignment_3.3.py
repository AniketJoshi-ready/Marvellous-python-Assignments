def main():
    countnum=int(input("give me count of numbers wanted in list  N :"))
    
    data=list()

    print("enter the  numbers  : ")
    for i in range(countnum):
        num=int(input())
        data.append(num)
    print("list of given number = ",data)


    min_num=data[0]       # we have to just assume the min number as a first number in list 

    for ele in data:          # iterate that number assumed number in the list and compare it with each element 
        if min_num>ele:       # until new min number not get , when it appear then that number is assumed to be the latest min number and so on we get the minimum number in list
            min_num=ele


    print("minimum number in given list is : ",min_num)





if __name__=="__main__":
    main()