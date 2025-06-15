import schedule
import datetime
import time
def display():
   print(" Do Coding !  ",datetime.datetime.now())


def main():
    schedule.every(30).minutes.do(display)
    


    print("application is in waiting state :")
    while True:
      schedule.run_pending() 
      time.sleep(1)


if __name__=="__main__":
    main()    