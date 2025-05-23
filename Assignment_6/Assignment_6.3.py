def main():
    num=int(input("eneter the number :"))
    print("table of given number ") 
    for i in range(1,11):
        table=num*i
    
        print(num,'*',i,"=",table) 
       
if __name__=="__main__":
    main()    