import pandas as pd
import numpy as np
import os
from datetime import date
import xlrd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from geopandas import GeoDataFrame

pd.set_option("display.max_columns", 55)

path = 'C:/Users/ghodg/Desktop/Project Data/Tax Lien'

csv_concat = glob.glob(os.path.join(path, "*.xlsx"))
files = [f for f in csv_concat if 'liensale' in f]

frames = []
boroughs = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
counter = 0
for i in files:
    df = pd.read_excel(i, encoding='utf-8')
    df['Borough'] = boroughs[counter]
    counter += 1
    frames.append(df)

concat_df = pd.concat(frames, ignore_index=True, sort=False)
concat_df.head()
concat_df.info()
concat_df.columns = concat_df.columns.str.replace(' ', '_')
concat_df.columns = concat_df.columns.str.lower()
concat_df['zip_code'] = concat_df['zip_code'].fillna(0)

concat_df.zip_code.value_counts()
concat_df['water_debt_only'].value_counts()

# Mapping NYC Zip Codes
zip_codes = GeoDataFrame.from_file('C:/Users/ghodg/Desktop/Project Data/Tax Lien/Zip Code Data/ZIP_CODE_040114/'
                                   'ZIP_CODE_040114.shp')
zip_codes['zip_code'] = zip_codes['ZIPCODE'].astype(int)
concat_df['zip_code'] = concat_df['zip_code'].astype(int)

counts = concat_df['zip_code'].value_counts()
counts = counts.to_frame(name='count_buildings')
counts = counts.reset_index()
counts = GeoDataFrame(counts.merge(zip_codes, how='left', left_on='index', right_on='zip_code'))
counts = counts.dropna()

# Plotting the map and colorbar
norm = colors.Normalize(vmin=counts.count_buildings.min(), vmax=counts.count_buildings.max())
cbar = plt.cm.ScalarMappable(norm=norm, cmap='Blues')

fig, ax = plt.subplots(figsize=(10, 10))
counts.plot(column='count_buildings', cmap='Blues', legend=False, alpha=1, linewidth=0.5, edgecolor='black', ax=ax)
ax_cbar = fig.colorbar(cbar, ax=ax, fraction=0.046, pad=0.04)
ax_cbar.set_label('# of Buildings')
plt.title('60 Day Lien Sale by Zipcode', size=20)
plt.axis('off')
plt.show()

cur_date = date.today().strftime("%m_%d_%Y")
plt.savefig('C:/Users/ghodg/Desktop/Project Data/Tax Lien/Graphs/60_day_liensale_by_zip_code_{}.png'.format(cur_date))


