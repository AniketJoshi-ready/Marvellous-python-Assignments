import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    
    df = pd.DataFrame(data)
    print("Original Data is : ")
    print(df)

    '''print("Normalized data using Pandas : ")
    Math_norm_pd = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())
    print(Math_norm_pd)'''

    print("Normalized data  of maths marks using MinMaxScaling : ")
    scaler = MinMaxScaler()
    Math_norm_MinMaxScaling  = scaler.fit_transform(df[['Math']])
    print(Math_norm_MinMaxScaling)

def main():
    Dataframe()

if __name__ == "__main__":
    main()