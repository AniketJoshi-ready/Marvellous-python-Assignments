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



   

    print("Gemder grouped Average Marks are : ")
    df = df.groupby('Gender')[['Math','Science','English']].mean()
    print(df)

def main():
    Dataframe()

if __name__ == "__main__":
    main()