import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    
    df = pd.DataFrame(data)
    print("Original Data is : ")
    print(df)

    df['Gender'] = ['Male','Male','Female'] 
    print("Updated Data : ")
    print(df)

    encoder = OneHotEncoder(handle_unknown='ignore',sparse_output=False).set_output(transform='pandas')
    encoded_data = encoder.fit_transform(df[['Gender']])
    print("Encoder output : ")
    print(encoded_data)

    df = pd.concat([df,encoded_data],axis=1).drop(columns=['Gender'])
    print("Final output : ")
    print(df)

def main():
    Dataframe()

if __name__ == "__main__":
    main()