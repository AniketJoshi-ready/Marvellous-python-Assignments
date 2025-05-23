def main():
    num=int(input("eneter the number : "))
    square=lambda x: x**2 
    cube=lambda y: y**3
    print("square of number  :",square(num))
    print("cube of number  :",cube(num))


if __name__=="__main__":
    main()    