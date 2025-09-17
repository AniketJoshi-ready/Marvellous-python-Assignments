import pandas as pd 
import numpy as np
def main():
    data={"marks":[85,np.nan,90,np.nan,95]}

    df=pd.DataFrame(data)
    print(df)

    df['changed_marks'] = df['marks'].interpolate()  # used linear method  # linear polynomial curve data ,time data ,spline smooth curve
    print("After Linear Interpolation:\n", df)

    


if __name__=="__main__":
    main()    