import schedule
import datetime
import time

def display():
    print("Jay Ganesh",datetime.datetime.now())

def main():
    schedule.every(2).seconds.do(display)
    


    print("application is in waiting state :")
    while True:
      schedule.run_pending() 
      time.sleep(1)


if __name__=="__main__":
    main()    