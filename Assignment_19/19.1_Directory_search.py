import sys
import os
def main():
    directory=sys.argv[1]
    extension=sys.argv[2]
    
    
    for foldername,subfoldername,filename in os.walk(directory):
        for ele in filename:
            if ele.endswith(extension): # to attach extension to file as .txt .doc .pdf
             print(ele)

if __name__=="__main__":
    main()    