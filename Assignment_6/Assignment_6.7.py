size=5
print("enter five numbers : ")
label=False
ele=0
for i in range(1,size+1):
    max_num=ele
    ele=int(input())
    
    if max_num>ele:
        label=True
    else:
        pass
    

if label==True:
    print("max number is :  ",max_num)
    
