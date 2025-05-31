import threading
# without using time module we can delay threads by threading function Timer(argu1_sec,argu2_function)
def display():
    for i in range(1,6):
        print(i)
#def delay():        not needed now
#    print("after 1 second :")     this can be used for passing delay func to lovely Timer (second , func ) which display bhidu stmnt

def main():
    t1=threading.Thread(target=display)
    t2=threading.Thread()                 # if we want to display further function after delay there is no need of defining it in next threads
    t3=threading.Thread()

    t1.start()
    t1.join()
    timer=threading.Timer(1,display)
    timer.start()
    timer.join()

    t2.start()
    t2.join()
    timer=threading.Timer(1,display)
    timer.start()
    timer.join()

    t3.start()
    t3.join()
    
    


if __name__=="__main__":
    main() 