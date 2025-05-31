import threading
from functools import reduce
add_ev=0
add_odd=0
def even(LIST):
    global add_ev
    for i in LIST :
        if i % 2==0:
           add_ev=add_ev+i
        else:
           pass
    print("addition of even list element : ",add_ev)
def odd(LIST):
    global add_odd
    for i in LIST :
        if i % 2!=0:
           add_odd=add_odd+i
        else:
           pass
    print("addition of odd lsit element : ",add_odd)

              

def main():
    size=int(input("size of list numbers : "))
    data=[]
    print("enter the numbers bhiduuu : ")
    for i in range (size):
        num=int(input())
        data.append(num)
    print("we have formed your list of given numbers bhiduuu : ",data)
    
    #data=[1,2,3,4,5,6]
    evenlist=threading.Thread(target=even,args=(data,))
    oddlist=threading.Thread(target=odd,args=(data,))

    evenlist.start()
    evenlist.join()

    oddlist.start()
    oddlist.join()

  

    print("end of main raja")




if __name__=="__main__":
    main()  