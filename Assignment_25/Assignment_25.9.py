import pandas as pd 
def main():
    data={"marks":[45,67,88,32,65]}

    df=pd.DataFrame(data)

    print(df)

    df["updated_data"]=df["marks"].where(df["marks"]>50,other="Fail")

    print(df)



if __name__=="__main__":
    main()    