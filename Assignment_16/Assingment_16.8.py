def main():
    filename="blank.txt"
    final="unblank.txt"

   # strip only leading and trailing whispaces removed 
   

    with open(filename,"w") as file :
        file.write("                 chak de india \n         my fav team mumbai indians \n")

    with  open(filename,"r") as file :     
        s=file.readlines()
        space_del=s[0].strip()
        space_del1=s[1].strip()   # or     for i in s    :     spacedel=i.strip
    

    with  open(final,"w") as file : 
        file.write(space_del)
        file.write(space_del1)
        

if __name__=="__main__":
    main()    