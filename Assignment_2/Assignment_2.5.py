def main():
    num=int(input("enter number : "))
    label=True                                 # must must must step bhiduuu should globally declare 
    if num==1 or num==0:
        print(" 0 and 1 are not considered as prime number ")
    else:
        for i in range (2,num):
            if num%i==0:
                label=False
        
    if label==False:
        print(num, "  not a  prime number")
    else:
        print(num," is  prime number")  





if __name__=="__main__":
    main()        

                    

           