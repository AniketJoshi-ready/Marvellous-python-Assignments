import sys
# input file abc.txt output file demo.txt
def main():
    inputfile=sys.argv[1]
    outputfile=sys.argv[2]

    source=open(inputfile,"r")
    destination=open(outputfile,"w")

    contents=source.read()
    destination.write(contents)

    

if __name__=="__main__":
    main()    