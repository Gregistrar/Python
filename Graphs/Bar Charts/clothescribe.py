import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# After setting ggplot, these are the params we have started using as defaults
plt.rcParams['font.sans-serif'] = 'Helvetica'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['grid.color'] = 'grey'
plt.rcParams['grid.linewidth'] = 1
plt.rcParams['grid.alpha'] = 0.2
plt.rcParams["axes.edgecolor"] = "black"
from adjustText import adjust_text

path = ('~/downloads/clothescribe.csv')
path = ('~/downloads/only_free_users.csv')
path = ('~/downloads/paid_users.csv')
path = ('~/downloads/paid_users_free_month.csv')

clothes = pd.read_csv(path)
clothes.info()
clothes.head()

# Category of clothes DF
clothes_cat = clothes[['category']]
category = clothes_cat.groupby('category')['category'].count()
plt.clf()

ax = category.plot(kind='bar', title ="Paid Users Free Month Orders by Clothing Category", figsize=(11, 11), legend=True, fontsize=12)
ax.set_xlabel("Clothing Category", fontsize=12)
ax.set_ylabel("# of Orders", fontsize=12)

plt.show()


# Type of clothes DF
clothes_type = clothes[['type']]
type = clothes_type.groupby('type')['type'].count()
type = type.sort_values(ascending=False)

plt.clf()

ax = type.plot(kind='bar', title ="Paid User Free Month Orders by Clothing Type", figsize=(9, 9), legend=True, fontsize=12)
ax.set_xlabel("Clothing Type", fontsize=12)
ax.set_ylabel("# of Orders", fontsize=12)

plt.show()

# Brand of clothes DF
clothes_brand = clothes[['brand']]
brand = clothes_brand.groupby('brand')['brand'].count()
brand = brand.sort_values(ascending=False)

plt.clf()

ax = brand.plot(kind='bar', title ="Paid User Free Month Orders by Clothing Brand", figsize=(8, 8), legend=True, fontsize=12)
ax.set_xlabel("Clothing Type", fontsize=12)
ax.set_ylabel("# of Orders", fontsize=12)

plt.show()

