import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def main():
    data={"age":[18,22,25,30,35]}

    df=pd.DataFrame(data)
    print(df)

    scaler=MinMaxScaler() 
    df["output"]=scaler.fit_transform(df[["age"]])
   # df=pd.concat([df,df["output"]],axis=1)  not necessary becoz we have converted above into dataframe as new column


    print(df)

if __name__=="__main__":
    main()    