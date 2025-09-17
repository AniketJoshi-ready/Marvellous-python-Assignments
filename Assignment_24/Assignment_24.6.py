import pandas as pd

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
    
    count = 0 
    for i in df['status'] :
        if i == 'pass':
            count += 1
    print("number of students passed are : ",count)

    # without using loop we have pandas feature like shape of column having value only pass
    print("number of students passed are : ",df[df['status'] == 'pass'].shape[0])



def main():
    Dataframe()

if __name__ == "__main__":
    main()