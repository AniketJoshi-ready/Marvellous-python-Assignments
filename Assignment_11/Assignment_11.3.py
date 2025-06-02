
sum=0
def digit_sum(num):
    global sum
    if num>0:
        digit=num%10    # to get last digit which is needed to add in previous sum
        sum=sum+digit   # last digit to be added in sum
        num=num//10     # to remove last digit so that not added digit number come in num variable
    else:
        return
    digit_sum(num) 
    return sum   

def main():
    value=int(input("enter value beta : "))
    result=digit_sum(value)
    print("recursive result of sum of digit bhiduu : ",result)

if __name__=="__main__":
    main()    