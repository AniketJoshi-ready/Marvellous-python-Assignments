import threading 
#import os
count_l=0
count_up=0
count_d=0
#string="AnikeT10902@"
def Lowerbeta(STRING):
    print("small thread  name and tid :   ",threading.current_thread().name," = ",threading.get_native_id())
    global count_l
    for i in STRING:
        r=i.islower()
        if r:
            count_l=count_l+1
        else:
            pass
    print("count of  lowercase charecter in given string broo : ",count_l)        
          
def Upperbeta(STRING):
    print("capital thread name and  tid : ",threading.current_thread().name," = ",threading.get_native_id())
    global count_up
    for i in STRING:
        r=i.isupper()
        if  r :
            count_up=count_up+1 
        else:
            pass
    print("count of  uppercase charecter in given string broo : ",count_up)

def Digitsbeta(STRING):
    print("digits thread name and  tid :  ",threading.current_thread().name," = ",threading.get_native_id())
    global count_d
    for i in STRING:
        r=i.isdigit()
        if  r:
          count_d=count_d+1
        else:
            pass        
    print("number of digits in given string broo : ",count_d)
def main():
    string=str(input("bhiduuu pehle string enter karle samjhya kya  : "))
    small=threading.Thread(target=Lowerbeta,args=(string,))
    capital=threading.Thread(target=Upperbeta,args=(string,))
    digits=threading.Thread(target=Digitsbeta,args=(string,))


    small.start()
    small.join()
    
    capital.start()
    capital.join()

    digits.start()
    digits.join()

    print("end of main bhiduu samjhya kya ")
                           
if __name__=="__main__":
    main()    