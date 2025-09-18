import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
def main():
    diabetes=pd.read_csv("Marvellousdiabetes.csv")

    print(diabetes.columns)

    print(diabetes.head())

    X=diabetes.drop(columns=["Outcome"])
    Y=diabetes["Outcome"]

    print(X.shape)
    print(Y.shape)


    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size= 0.2,random_state=42)

    model=DecisionTreeClassifier()

    model.fit(X_train,Y_train)

    Y_pred=model.predict(X_test)  # windows iternal book 

    accuracy=accuracy_score(Y_test,Y_pred)

    print("accuracy is ",accuracy*100)

if __name__=="__main__":
    main() 