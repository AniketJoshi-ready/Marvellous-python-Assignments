import psutil
def main():
    
    for elements in psutil.process_iter(["pid","name","username"]):
       pid=elements.info["pid"]
       name=elements.info["name"]
       username=elements.info["username"]
       #started=elements.info[]
       
    
       print(pid,end=" ")
       print(name,end=" ")
       print(username)
       #print(status)
       #print(started)
       


if __name__=="__main__":
    main()    