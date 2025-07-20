import pandas as pd
def main():
    Data= {"Name": ["Amit","Sagar","Pooja"],
           "Math":[85,90,78],
           "Science":[92,88,80],
           "English":[75,85,82]}
    df=pd.DataFrame(data=Data)

    print("i have created this dataframe buddy :\n ",df)

    print("shape of dataframe : ",df.shape)
    print("columns of dataframe : ",df.columns)
    print("data types of dataframe :\n ",df.dtypes)
    
    
    

if __name__ =="__main__":
    main()    