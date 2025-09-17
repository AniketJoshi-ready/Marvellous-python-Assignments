# label coding 
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    data={'city':['pune','mumbai','delhi','pune','delhi']}

    df=pd.DataFrame(data)

    print(df)

    # label encoder object create karo and fit transform ko call karo beta

    encoder=LabelEncoder()
    df['label_encoded']=encoder.fit_transform(df['city'])
    
    print("updated data : \n")
    print(df)


if __name__=="__main__":
    main()    