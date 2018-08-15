from tabula import read_pdf
import pandas as pd

df = read_pdf('2017ElkPopulationEstimates.pdf')

df.columns = ["page", "dau", "estimate", "unknown"]
#df = pd.to_numeric(df, errors='coerce')


print(df.shape())

columns = list(df)
