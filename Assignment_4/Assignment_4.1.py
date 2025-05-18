def main():
    num=int(input(" enter the number : "))
    fn=lambda num : num**2     # when assign var to function then it acts as a fn name so u have to call it and assifn paremeter to it 
    result=fn(num)
    print("power of two for given num : ",result)

    print()
if __name__=="__main__":
    main() 