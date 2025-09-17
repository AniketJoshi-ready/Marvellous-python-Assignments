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
     
    # we have considered Amit as sagar 
    sagar_marks = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].iloc[0]

    plt.figure(figsize=(6,4))
    plt.pie(sagar_marks.values, labels=sagar_marks.index, autopct='%1.1f%%')
    plt.title("Sagar's Subject Marks")
    plt.show()

def main():
    Dataframe()

if __name__ == "__main__":
    main()