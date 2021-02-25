import pandas as pd

df = pd.read_csv("https://covidtracking.com/api/states.csv")

def dataPull(index):
     return df.iloc[index].deathIncrease, df.iloc[index].positiveIncrease


    