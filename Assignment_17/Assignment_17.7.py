import schedule
import datetime
import time
import sys
def backup(fname):
   timestamp=time.ctime()
   fobj=open(fname,"r")
   data=fobj.read()

   fobj=open("backup.txt","a")
   fobj.write(data)
   fobj.write("file backup done at : "+timestamp+"\n")
   
def main():
    filename=sys.argv[1]

    schedule.every(2).seconds.do(backup,filename)
    
    print("application is in waiting state :")
    while True:
      schedule.run_pending() 
      time.sleep(1)

if __name__=="__main__":
    main()    