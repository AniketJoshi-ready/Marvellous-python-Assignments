def main():
    string=str(input("eneter the string bhiduuu chal patapat bol : "))
    label=False
    i=0
    j=-1
    l=len(string)
    while i<l:
        if string[i]==string[j]:
            label=True
        i=i+1
        j=j+1    
            
                
    if label==True:
        print(string," is  pallindrome ") 
    else:
        print(string,"is   not pallindrome")               


if __name__=="__main__":
    main()    