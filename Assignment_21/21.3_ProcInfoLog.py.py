import psutil
import os

def createlog(foldername):
    if not os.path.exists(foldername):
        os.mkdir(foldername)
    filename=os.path.join(foldername,"log.txt")
    fname=open(filename,"w")
    
    data=processinfo()

    for value in data :
        fname.write("%s \n" %value)
    fname.close()    


def processinfo():
    list_process=[]
    for ele in psutil.process_iter():
        info=ele.as_dict(attrs=["pid","name","username"])
        list_process.append(info)
    return list_process            

    

def main():
    dirname="demo"
    createlog(dirname)

    

if __name__ == "__main__":
    main()
