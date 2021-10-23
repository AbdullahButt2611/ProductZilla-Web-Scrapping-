import pandas as pd

data = pd.read_csv('ScrapFileOrignal.csv',index_col=False)
name = []
name = data.loc[:,"Names"]
print(name)



