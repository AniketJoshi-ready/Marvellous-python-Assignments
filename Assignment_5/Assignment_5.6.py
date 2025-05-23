def converter(C):
    F=(C* (9/5))+32
    return F
def main():
    Celcius_temp=float(input("enter celcius temperature : "))
    result=converter(Celcius_temp)
    print("Farenheite temperature = ",result)
if __name__=="__main__":
    main()    
