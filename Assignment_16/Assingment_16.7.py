def main():
    filename="marks.txt"
    fname=open(filename,"w")

    fname.write("student name : aniket  \nmarks1 :87")
    fname.write("\n")
    fname.write("student name : anamika  \nmarks2 :700")
    fname.close()

    with open(filename,"r") as file :
        f=file.readlines()
        marks1=int(f[1].strip("marks1 :"))
        marks2=int(f[3].strip("marks2 :"))
        if  marks1>marks2  :
            print("aniket has highest marks ")
        else:
            print("anamika has highest marks ")    

    


    


if __name__=="__main__":
    main()    