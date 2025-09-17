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

    plt.figure(figsize=(8,6))
    plt.hist(df['Math'],color='skyblue')
    plt.title('Distribution of Maths Marks')
    plt.xlabel('Maths Marks')
    plt.ylabel('Number of Students')
    plt.grid(True)
    plt.show()
    
def main():
    Dataframe()

if __name__ == "__main__":
    main()