def chkNum(Input):
    if Input %2==0:
        print( "Output = even number ")
    else:
        print("Output = odd number ")    


def main():
    print("input = ", end=" ")
    Input=int(input())
    chkNum(Input)
    print("thank you so much ")       


if __name__=="__main__":
    main()    