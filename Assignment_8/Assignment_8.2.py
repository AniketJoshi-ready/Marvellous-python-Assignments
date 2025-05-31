import threading
def evfactor(num):
    print("even factors of ",num," are : ")
    for ele in range(1,num):
        if num%ele==0 and ele%2==0 :
            print(ele)
        else:
            pass


def odfactor(num):
    print("odd factors of ",num," are : ")
    for ele in range(1,num):
        if num%ele==0 and ele%2!=0 :
            print(ele)
        else:
            pass 

def main():
    number=int(input("enter the number : "))


    evenfactor=threading.Thread(target=evfactor,args=(number,))
    oddfactor=threading.Thread(target=odfactor,args=(number,))

    evenfactor.start()
    evenfactor.join()

    oddfactor.start()
    oddfactor.join()

    print("exit from main ")
if __name__=="__main__":
    main()  