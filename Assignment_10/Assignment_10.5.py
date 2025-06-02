from functools import reduce

def prime(num):
    label=True       # local label should be declare 
    if num==1 or num==0:
        pass
    else:
        for i in range(2,num):
            if num%i==0:
                label=False
                   
        return label
def main():
    size=int(input("enter the size of list : "))
    data=[]
    print("enter the value : ")
    for i in range(size):
        num=int(input())
        data.append(num)
    print("list of element = ",data)

    fdata=list(filter(prime,data)) 
    print("filtered output = ",fdata)

    mdata=list(map(lambda x: x*2 ,fdata))
    print("mapped output = ",mdata)

    rdata=reduce(lambda x,y : x if x>y else y ,mdata)
    print("reduced output = ",rdata)   
if __name__=="__main__":
    main() 