def main():
    filename="chandu.txt"
    with open(filename,"r") as file :
    
        for lines in file:
           count_words=len(lines.split())
           if count_words > 5 :
              print(lines)
      
    

if __name__=="__main__":
    main()    