import pandas as pd 
from sklearn.model_selection import train_test_split
def main():
    data ={'Age':[22,25,47,52,46,56],'purchase':[0,1,1,0,1,0]}
    df = pd.DataFrame(data)
    print(df)

    X=df[['Age']]     # feature
    y=df['purchase']  # label

    X_TRAIN,X_TEST,Y_TRAIN,Y_TEST=train_test_split(X,y,random_state=42,test_size=0.2)

    print("X-TRAIN:\n",X_TRAIN)
    print("X-TEST:\n",X_TEST)

    print("Y-TRAIN:\n",Y_TRAIN)
    print("Y-TEST:\n",Y_TEST)

if __name__=="__main__":
    main()    