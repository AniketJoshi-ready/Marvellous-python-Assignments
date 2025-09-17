import pandas as pd
import matplotlib.pyplot as plt

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    
    df = pd.DataFrame(data)
    print("Original Data is : ")
    print(df)

    df['total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    print(df)

    df['status'] = df['total'].apply(lambda x: 'pass' if x >= 250 else 'fail')
    print(df)
    
def main():
    Dataframe()

if __name__ == "__main__":
    main()