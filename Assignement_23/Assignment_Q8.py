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
    amit_marks = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].iloc[0]

    plt.figure(figsize=(6, 4))
    plt.plot(amit_marks.index, amit_marks.values, marker='o', linestyle='-', color='blue')
    plt.title("Amit's Marks Across Subjects")
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.grid(True)
    plt.show()

def main():
    Dataframe()

if __name__ == "__main__":
    main()