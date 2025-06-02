sum=0
def sum_of_N(n):
    global sum
    if n>0:
        sum=sum+n
        n=n-1
    else:
        return
    sum_of_N(n)
    return sum    


def main():
    N=int(input("enter N number : "))
    result=sum_of_N(N)
    print(result)

if __name__=="__main__":
    main()  