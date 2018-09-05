import pandas as pd
import os
import sqlalchemy
import glob


path = '/Users/ghodgson/desktop/Teacher Files/'
# path = '/Users/ghodgson/Desktop/Academic Outliers October .xlsx'

# Not used in this current concat
#files = [f for f in os.listdir(path) if f.endswith('.xlsx')]

# Joining the .csv files together in the path
csv_concat = glob.glob(os.path.join(path, "*.xlsx"))

frames = {}
# Used to actually concat the files together into one document
for file in csv_concat:
    df_file = pd.read_excel(file)
    df_file = df_file.drop(columns=['Student Last Name', 'Student First Name', 'Student Id'])
    df_file = df_file.drop_duplicates()
    df_file['file_name'] = file
    frames[file] = df_file
concat_df = pd.concat(frames, ignore_index=True)
concat_df.head()
concat_df.info()
concat_df.to_csv('~/desktop/teacher_concat.csv', encoding='utf-8')
