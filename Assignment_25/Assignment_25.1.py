import numpy as np
import pandas as pd
def main():

    data = {"salary":[25000,27000,29000,31000,50000,100000]}
    df = pd.DataFrame(data)
    print(df)
    # Step 1: Calculate Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = df['salary'].quantile(0.25)
    Q3 = df['salary'].quantile(0.75)

    # Step 2: Calculate IQR
    IQR = Q3 - Q1

    # Step 3: Find lower and upper bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Step 4: Detect outliers
    outliers = df[(df['salary'] < lower_bound) | (df['salary'] > upper_bound)]

    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("\nOutliers:")
    print(outliers)

if __name__=="__main__":
    main()