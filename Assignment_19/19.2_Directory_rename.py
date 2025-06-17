import sys
import os
def main():
    directory=sys.argv[1]
    extension=sys.argv[2]
    extension_convert=sys.argv[3]

    
    
    for foldername,subfoldername,filename in os.walk(directory):
        for ele in filename:
            if ele.endswith(extension):
             print("old :" ,ele) # to attach extension to file as .txt .doc .pdf
             fele=ele.replace(extension,extension_convert)
             print("new : ",fele)

            

if __name__=="__main__":
    main()     