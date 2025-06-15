import datetime
import time
import schedule
def display():
    s=datetime.datetime.now()
    with open("marvellous.txt","a") as file :
        file.write("after evry 5 minutes i am comming : "+str(s))
        file.write("\n")


def main():
    schedule.every(5).minutes.do(display)
    



    print("application is in waiting state : ")

    while True :
        schedule.run_pending()
        time.sleep(1)

    
if __name__=="__main__":
    main()    