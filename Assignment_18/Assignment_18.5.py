import sys
def main():
    filename="demo.txt"
    fname=open(filename,"r")
    content=fname.read()
    ret=content.count("dhonduuuu")
    print("frequency = ",ret)
if __name__=="__main__":
    main()    