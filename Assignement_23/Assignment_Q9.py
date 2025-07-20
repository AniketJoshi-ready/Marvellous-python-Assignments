import pandas as pd
import numpy as np

def Dataframe():
    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }

    df2 = pd.DataFrame(data2)
    print("Original DataFrame with Missing Values:")
    print(df2)

    df2[['Math', 'Science']] = df2[['Math', 'Science']].fillna(df2[['Math', 'Science']].mean())

    print("\nDataFrame after Filling Missing Values with Column Mean:")
    print(df2)

def main():
    Dataframe()

if __name__ == "__main__":
    main()