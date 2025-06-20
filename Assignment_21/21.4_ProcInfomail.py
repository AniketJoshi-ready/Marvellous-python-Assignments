import psutil
import os
import sys
import smtplib
from email.message import EmailMessage

def sendmail(filepath):
    fobj=open(filepath,"rb")
    data=fobj.read()

    msg= EmailMessage()
    msg.add_attachment(data,maintype="file",subtype="log",filename=filepath)

    msg["Subject"] = "log file of current processes "
    msg["From"] = "annizomby22.1166@gmail.com"
    msg["To"]="govj2002@gmail.com"

    s= smtplib.SMTP("smtp.gmail.com",)
    s.starttls()
    s.login("annizomby22.1166@gmail.com","mera password mahan hai") 
    s.send_message(msg)
    s.quit()



def createlog(foldername):
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    filename=os.path.join(foldername,"log.txt")
    fname=open(filename,"w")
    
    data=processinfo()

    for value in data :
        fname.write("%s \n" %value)
    fname.close()    

    return filename
def processinfo():
    list_process=[]
    for ele in psutil.process_iter():
        info=ele.as_dict(attrs=["pid","name","username"])
        list_process.append(info)
    return list_process            

    

def main():
    dirname="demo"
    path=createlog(dirname)
    sendmail(path)

    

if __name__ == "__main__":
    main()