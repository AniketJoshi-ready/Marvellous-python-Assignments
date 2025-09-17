# one hot encoding 

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
   data = {'department':['HR','IT','FINANACE','HR','IT']}

   df=pd.DataFrame(data)

   print(df)

   # creating object of one hot encoder

   encoder=OneHotEncoder(sparse_output=False).set_output(transform='pandas')
   encoded_df=encoder.fit_transform(df[['department']])

   df = pd.concat([df, encoded_df], axis=1)
   
   print("updated data : \n")
   print(df)

if __name__== "__main__":
   main()
