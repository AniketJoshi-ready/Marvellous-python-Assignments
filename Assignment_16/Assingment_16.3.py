def display():
    count_line=0
    count_words=0
    count_letter=0
    
    with open("data.txt","r") as file:     #with open is for  opening and auto closing block 
        for line in file:
            count_line=count_line+1
            count_words=count_words+len(line.split())    # bhiduu log split() gives whitespaces that is blankspaces so we wrote in evry line we just add length of that whitespaces 
            for letter in line:
                count_letter=count_letter+1
               
            

        print("no. of lines : ",count_line)
        print("no. of words : ",count_words)
        print("no. of letters : ",count_letter)


display()

        
        
