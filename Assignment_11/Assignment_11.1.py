i=1
def display(n):
        global i 
        if i<=n:
            print(i)
            i=i+1 
        else:
            return    # this is very imp step if not then i got infinity error . This  display func will keep calling itself forever because n never changes, and there's no condition to stop the recursion. so need return 
            
        display(n)     
         
def main():
    display(5)

if __name__=="__main__":
    main()