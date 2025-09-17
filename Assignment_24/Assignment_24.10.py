import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}

    df = pd.DataFrame(data)
    print("Original Data is : ")
    print(df)

    sns.boxplot(x="Name",y="English",data=df)
    plt.title('Distribution of English Marks')
    plt.show()

def main():
    Dataframe()

if __name__ == "__main__":
    main()