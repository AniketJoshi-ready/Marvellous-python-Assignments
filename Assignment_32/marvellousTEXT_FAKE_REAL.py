import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,ConfusionMatrixDisplay
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

def main():
    df_fake=pd.read_csv("Fake.csv")
    df_true=pd.read_csv("True.csv")

    #print(df_fake)
    #print(df_true)
    
    # adding columns
    df_fake['label'] = 0   # fake
    df_true['label'] = 1   # real

    df=pd.concat([df_fake,df_true],ignore_index=True)
    df=shuffle(df,random_state=42).reset_index(drop=True)
    print(df.info())

    print("tf-idf is in process:")
    # Feature extraction: TF-IDF
    # Set max_features=None to use full vocabulary, or an integer to limit size for speed.
    MAX_FEATURES = 20000   # e.g. 20000 for faster runs; None uses all features
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7, max_features=MAX_FEATURES, ngram_range=(1,2))
    X = tfidf.fit_transform(df["title"]+" "+ df["text"])
    y = df['label'].values


    print("training is in process")
    # Train/test split (stratify to keep class balance)
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

    # Model training
    lr = LogisticRegression(max_iter=1000)               # logistic regression
    dt = DecisionTreeClassifier(random_state=42)         # decision tree

    # Fit individual models
    lr.fit(X_train, Y_train)
    dt.fit(X_train, Y_train)

    pred_lr=lr.predict(X_test)
    pred_dt=dt.predict(X_test)

    print("voting classifier in process : ")
    voting_hard=VotingClassifier(estimators=[("logr",lr),("dectree",dt)], voting="hard" )
    voting_soft=VotingClassifier(estimators=[("logr",lr),("dectree",dt)], voting="soft" )

    voting_hard.fit(X_train, Y_train)
    voting_soft.fit(X_train, Y_train)

    pred_hard=voting_hard.predict(X_test)
    pred_soft=voting_soft.predict(X_test)
    
    # Results :
    Accu_lr=accuracy_score(Y_test,pred_lr)*100
    Accu_dt=accuracy_score(Y_test,pred_dt)*100


    Accu_hv=accuracy_score(Y_test,pred_hard)*100
    Accu_sv=accuracy_score(Y_test,pred_soft)*100

    cm_lr=confusion_matrix(Y_test,pred_lr)
    cm_dt=confusion_matrix(Y_test,pred_dt)

    cm_hv=confusion_matrix(Y_test, pred_hard)
    cm_sv=confusion_matrix(Y_test, pred_soft)

    cr_lr=classification_report(Y_test,pred_lr)
    cr_dt=classification_report(Y_test,pred_dt)

    cr_hv=classification_report(Y_test,pred_hard)
    cr_sv=classification_report(Y_test,pred_soft)






    
    print("accuracy individual logistic regrssion : ",Accu_lr)
    print("accuracy individual decision tree  : ",Accu_dt)


    print("accuracy hard voting : ",Accu_hv)
    print("accuracy soft voting : ",Accu_sv)

    

    # confusion matrix
    print("confusion matrix individual logistic regrssion : ",cm_lr)
    print("confusion matrix individual decision tree  : ",cm_dt)

    print("Confusion Matrix hard voting :\n",cm_hv )
    print("Confusion Matrix soft voting :\n", cm_sv)


    # classification report
    print("classification report individual logistic regrssion : ",cr_lr)
    print("classification report individual decision tree  : ",cr_dt)


   
    print("Classification Report hard voting :\n", cr_hv)
    print("Classification Report soft voting :\n", cr_sv)

    # plottings
    list_cm=[cm_lr,cm_dt,cm_hv,cm_sv]
    for i in list_cm:
        disp = ConfusionMatrixDisplay(confusion_matrix=i, display_labels=[0, 1])
        disp.plot(cmap="Blues")
        plt.title("Confusion Matrix ")
        plt.show()



    



    
if __name__=="__main__":
    main()    