import pandas as pd

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    
    df = pd.DataFrame(data)
    print("Data is : ",df)


    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
    print("New Data is : ",df)


    Filtered_df = df[df['Science'] > 85]
    print("Students who scored more than 85 in Science :",Filtered_df)
    

def main():
    Dataframe()

if __name__ == "__main__":
    main()