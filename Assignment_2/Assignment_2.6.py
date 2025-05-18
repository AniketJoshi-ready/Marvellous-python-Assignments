def main():
    num=int(input("enter the number : "))
    r=num         # ye he rows 
    c=num          # ye he columns
    for i in range(1,r+1):    # i gives you rows iteration
       # print("i",i)
        for j in range(c-i+1,0,-1):       # j gives you actual * count in that iterated(i) row
            #print("j",j," * ",end="  ")
            print(" * ",end="  ")
        print("  ")    


if __name__=="__main__":
    main()


