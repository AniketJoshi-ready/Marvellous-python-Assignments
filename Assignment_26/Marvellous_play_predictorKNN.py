import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def Displayinfo_dataset(dataset):
    # some basic display for just review of whether corrctly dataset is loadded pr not bhidduuu 
    print(dataset.shape)
    print(dataset.head())
    print(dataset.tail())
    
    # information about the columns
    print(dataset.info())
    # statestical information is important bhidduuuu
    print(dataset.describe())

def ENCODING_DATASET(dataset):
    # Encoding
    fencod=LabelEncoder()
    lencod=LabelEncoder()
     
    # feature ecoder is done  :
    dataset["Whether"]=fencod.fit_transform(dataset["Whether"])
    dataset["Temperature"]=fencod.fit_transform(dataset["Temperature"])

    # label encoder is done :
    dataset["Play"]=lencod.fit_transform(dataset["Play"])

    # just want to see beta sahi hua he ki nahi
    print(dataset) 

    return dataset  

def TRAIN_AND_TEST_MODEL(dataset):
    X=dataset[["Whether","Temperature"]]
    y=dataset["Play"]
    
    X_train,X_test,Y_train,Y_test= train_test_split(X,y,test_size=0.2,random_state=42)

    # Create and train model
    k=7
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, Y_train)

    # FOR Prediction
    y_pred = model.predict(X_test)  

    return y_pred ,Y_test,k

def CheckAccuracy(y_pred,Y_test,k):
    Accuracy=accuracy_score(Y_test, y_pred)*100
    print("Accuracy of model :",Accuracy )
    return Accuracy,k

def SAVE_ACCURACY_SCORE(Accuracy,k):
    # store in file.txt in this directory 
    with open("accuracy.txt", "a") as file:
      file.write(f" Accuracy of model when  k that n_neighbors is {k}  : {Accuracy:.2f}%\n")


def main():
    # first we have to load the data set 
    dataset=pd.read_csv("PlayPredictor.csv")

    Displayinfo_dataset(dataset)
    dataset=ENCODING_DATASET(dataset)
    y_pred,Y_test,k=TRAIN_AND_TEST_MODEL(dataset)
    Accuracy,k=CheckAccuracy(y_pred,Y_test,k)
    SAVE_ACCURACY_SCORE(Accuracy,k)



if __name__ == "__main__":
    main()    