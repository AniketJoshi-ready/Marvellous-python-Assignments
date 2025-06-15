import schedule
import datetime
import time

def display1():
    print("lunch time it is 1pm is it ?   :",datetime.datetime.now())
def display2():
    print("wrap up work it is 6 pm is it ?  : ",datetime.datetime.now())    

def main():
    

    schedule.every().day.at("13:00").do(display1)
    schedule.every().day.at("6:00").do(display2)
    
    print("application is in waiting state : ")

    while True :
        schedule.run_pending()
        time.sleep(1)


if __name__=="__main__":
    main()    