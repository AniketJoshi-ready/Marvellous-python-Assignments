def main():
    num=int(input("eneter the number : "))
    label=False
    if num==0 or num==1:
        print("0 and 1 are not considered as prime number bhidduuu ")
    else:
        for i in range(2,num):
            if num%i==0:
                label=True
              
        if label==True:
            print(num,"is not prime number bhiduuu")
        else:
            print(num,"is  prime number bhiduu")   
if __name__=="__main__":
    main()                     

