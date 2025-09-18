import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
def main():
    diabetes=pd.read_csv("Marvellousdiabetes.csv")

    print(diabetes.columns)

    print(diabetes.head())

    X=diabetes.drop(columns=["Outcome"])
    Y=diabetes["Outcome"]

    print(X.shape)
    print(Y.shape)

    x_train,x_test, y_train,y_test = train_test_split(X,Y,test_size=2,random_state=42)

    accuracy_scores = []
    k_range = range(1,21)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors = k)
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)   
        accuracy_scores.append(accuracy)

    plt.figure(figsize = (8,5))
    plt.plot(k_range, accuracy_scores, marker = 'o', linestyle = '--')
    plt.title("Accuracy vs K value")
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy of model")
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    best_k= k_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is : ",best_k)

    model = KNeighborsClassifier(n_neighbors = best_k)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("Final best accuracy is : ",accuracy*100)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

if __name__=="__main__":
    main() 