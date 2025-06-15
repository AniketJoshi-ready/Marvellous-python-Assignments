import schedule
import datetime
import time


def display():
    print("current data and time = ",datetime.datetime.now())


def main():
    print("current data and time ")
    schedule.every(60).seconds.do(display)
    


    print("application is in waiting state :")
    while True:
      schedule.run_pending() 
      time.sleep(1)


if __name__=="__main__":
    main()    