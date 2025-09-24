#breast-cancer-wisconsin detection using ensemble and comparint it with decision tree
# now we will do two algo of ensemble 1 Randomforest(bagging ) 2 gradient boost (boosting)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve
)
def main():
    # --------------------------
    # Step 1: Load dataset
    # --------------------------
    df = pd.read_csv("breast-cancer-wisconsin.csv")
    print(df)
    print("shape of dataframe :\n",df.shape)
    # for column ,datatype informarion 
    print(df.info())
    # Drop ID column if present
    if 'CodeNumber' in df.columns:
        df = df.drop(columns=['CodeNumber'])

    # --------------------------
    # Step 2: Preprocessing
    # --------------------------
    target_col = df.columns[-1]   # Target is last column =  cancer type  (label)
    features = [c for c in df.columns if c != target_col]   #(feature)

    # Convert features to numeric
    for c in features:
        df[c] = pd.to_numeric(df[c], errors='coerce')

    # Convert target: 2 = benign (0), 4 = malignant (1) for ease understanding 
    df[target_col] = pd.to_numeric(df[target_col], errors='coerce')
    df[target_col] = df[target_col].map({2: 0, 4: 1})

    # Impute missing feature values with median
    imp = SimpleImputer(strategy='median')
    df[features] = imp.fit_transform(df[features])

    # --------------------------
    # Step 3: Train-test split
    # --------------------------
    X = df[features]
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    # --------------------------
    # Step 4: Define models
    # --------------------------
    models = {
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
    }

    # --------------------------
    # Step 5: Train & Evaluate
    # --------------------------
    plt.figure(figsize=(8,6))

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print("="*60)
        print(f"{name}")
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

        # --------------------------
        # ROC Curve
        # --------------------------
        if hasattr(model, "predict_proba"):
            y_proba = model.predict_proba(X_test)[:, 1]
        else:  # for models without predict_proba
            y_proba = model.decision_function(X_test)

        fpr, tpr, _ = roc_curve(y_test, y_proba)
        roc_auc = roc_auc_score(y_test, y_proba)

        plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.3f})")

    # --------------------------
    # Step 6: Plot settings
    # --------------------------
    plt.plot([0,1], [0,1], 'k--')  # diagonal line
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve Comparison")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()
if __name__=="__main__":
    main()