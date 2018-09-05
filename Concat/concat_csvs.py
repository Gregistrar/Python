import pandas as pd
import os
import sqlalchemy
import glob

path = '/Users/ghodgson/downloads/nyseslat-2017-18'
# path = '/Users/ghodgson/Desktop/Academic Outliers October .xlsx'

# Not used in this current concat
files = [f for f in os.listdir(path) if f.endswith('.csv')]

# Joining the .csv files together in the path
csv_concat = glob.glob(os.path.join(path, "*.csv"))

# Used to actually concat the files together into one document
df_from_each_file = (pd.read_csv(f) for f in csv_concat)
concat_df = pd.concat(df_from_each_file, ignore_index=True)
concat_df.head()
concat_df.info()
concat_df.to_csv('~/desktop/nyseslat_reports_concat_SY17-18.csv', encoding='utf-8')
