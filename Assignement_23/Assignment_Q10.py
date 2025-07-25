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

    dropped_df=df.drop(["English"],axis=1)
    print("after droping : \n",dropped_df)

def main():
    Dataframe()

if __name__ == "__main__":
    main()