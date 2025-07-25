import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    
    df = pd.DataFrame(data)
    print("Data is : ",df)


    df['Total_Marks'] = df[['Math', 'Science', 'English']].sum(axis=1)
    print("New Data is : ",df)

    
    replace_df = df.replace('Pooja','Puja')
    print("Replaced data : ",replace_df)

    sorted_df = df.sort_values(by='Total_Marks',ascending=False)
    print("Sorted Data : ",sorted_df)

    plt.figure(figsize=(6,4))
    sns.barplot(data=df,x= 'Name', y='Total_Marks',hue="Name",palette='pastel')
    plt.title('Student Names vs Total Marks')
    plt.xlabel('Students')
    plt.ylabel('Total_Marks')
    plt.grid(True)
    plt.show()

    '''plt.figure(figsize=(6, 4))
    plt.bar(df['Name'], df['Total_Marks'], color=['skyblue', 'lightgreen', 'salmon'])
    plt.title('Student Names vs Total Marks')
    plt.xlabel('Students')
    plt.ylabel('Total_Marks')
    plt.grid(True)
    plt.show()'''

def main():
    Dataframe()

if __name__ == "__main__":
    main()