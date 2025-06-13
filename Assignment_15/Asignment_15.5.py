import sys
def count_str(filename,given_string):
    with open(filename,"r") as file:
        fread=file.read()
        frequency=fread.count(given_string)
    return frequency    
      

def main():
    fname=sys.argv[1]
    string=sys.argv[2]

    print("frequency of given string in the file : ",count_str(fname,string))
    


    

    

      
if __name__=="__main__":
    main()    