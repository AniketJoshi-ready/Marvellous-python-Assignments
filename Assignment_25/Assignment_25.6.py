import pandas as pd 
def main():
    data={'grade':['A+','B','A','C','B+']}
    df=pd.DataFrame(data)
    df['name_grade'] = df['grade'].replace({'A+': 'EXCELLENT', 'A':'VERY GOOD' ,'B+':'GOOD','B':'AVERAGE','C':'POOR'})

    print(df)
    

if __name__=="__main__":
    main()