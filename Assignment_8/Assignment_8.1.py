import threading
def evnum():
    count=1
    num=1
    print("even numbers : ")
    while count<21:
       if num%2==0 :
           print(num)
       else:
           pass
           
       count=count+1
       num=num+1  
       
def odnum():
    count=1
    num=1
    print("odd numbers : ")
    while count<21:
       if num%2==0 :
           pass
       else:
           print(num)
           
       count=count+1
       num=num+1 
                  

even=threading.Thread(target=evnum)
odd=threading.Thread(target=odnum)

even.start()
even.join()

odd.start()
odd.join()