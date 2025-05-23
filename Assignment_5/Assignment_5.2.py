# vowel or consonant check

def main():
    vowels=("a","e","i","o","u")
    #vowels="aeiou"        
    w=str(input("enter the charector : "))
    if w  in vowels:    # if we use in operator it will be easy to search out string charector in string or tuple or list  
        print(w," is a vowel ")
    else:
        print(w,"is a consonant ")    

   
if __name__=="__main__":
    main()