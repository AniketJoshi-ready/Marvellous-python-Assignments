import threading
import multiprocessing
import time
addition= 0
def sum():
    global addition
    for ele in range(1,10000001):
        addition=addition+ele
    print(addition)    
def main():
    s1=time.time()
    print("normal function sum : ")
    sum()
    e1=time.time()
    NT=e1-s1
    print("time for normal sum function execute  = ",NT)
    

    s2=time.time()
    T1=threading.Thread(target=sum)
    T1.start()
    T1.join()
    e2=time.time()
    TT=e2-s2
    print("time for thread T1  execute  = ",TT)


    s3=time.time()
    P1=multiprocessing.Process(target=sum)
    P1.start()
    P1.join()
    e3=time.time()
    PT=e3-s3
    print("processing for thread T1  execute  = ",PT)

    if PT>TT:
        if TT>NT:
            print("Multi-Processing time is greater and other two are taking less time")
        elif NT>PT :
            print("normal function execute tile is greater than other two methods ")
        else:
            print("threading time is the greater time than other two one ")
            



    

    print("end of main ")



if __name__=="__main__":
    main()  