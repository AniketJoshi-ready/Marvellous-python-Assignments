import threading
def displayforward():
    for i in range (1,51):
        print(i)
def displayreverse():
    for i  in range(50,0,-1):
        print(i)      
def main():
    thread1=threading.Thread(target=displayforward)
    thread2=threading.Thread(target=displayreverse)
    print("display 1 to 50")
    thread1.start()
    thread1.join()
    print("display 50 to 1")
    thread2.start()
    thread2.join()

    print("end of main ")
if __name__=="__main__":
    main()  