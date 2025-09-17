import pandas as pd 
from sklearn.model_selection import train_test_split 

def main():
    data={"age":[25,30,45,35,22], "salary":[50000,60000,80000,65000,45000], "purchased":[1,0,1,0,1]}
    df = pd.DataFrame(data)

    Features=df[["age","salary"]]
    Labels=df["purchased"]

    X_train,X_test,Y_train,Y_test=train_test_split(Features,Labels,test_size=0.4,random_state=42)

    print("trained data set : \n")
    print(X_train)
    print(Y_train)


    print("testing dataset : \n")
    print(X_test)
    print(Y_test)
if __name__=="__main__":
    main()    