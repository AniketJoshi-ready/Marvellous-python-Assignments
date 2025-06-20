import psutil
def main():
    running="Notepad.exe"
    for elements in psutil.process_iter(["name"]):
        if elements.info["name"]==running:
            print("yes darling ",running," is in running process in your pc ")
        
        
        
       # else:     can not write else it gives that much  senteces jitke  elements  are present in iterate 
           # print("no such process running")    
    
          
if __name__=="__main__":
    main()    