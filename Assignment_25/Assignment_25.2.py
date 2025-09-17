import pandas as pd 

def main():
    data={"Name":['A','B','C'], 'Age':[21.0,22.0,23.0]}

    df=pd.DataFrame(data)

    print(df)

    print("data type : ",df.dtypes)
    print("change data type",df["Age"].astype(int))

if __name__=="__main__":
    main()