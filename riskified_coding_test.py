"""
The dataframe attached has records of 1,000 objects with 3 columns:
# 1. shape - square, triangle (equilateral) or circle
# 2. color - blue, red, green or yellow
# 3. area - area size in square inches
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


riskified_df = pd.read_csv('C:/Users/ghodg/downloads/Analyst_Coding_Test.csv', encoding='utf-8')
riskified_df.info()
riskified_df.head()

"""
1. Draw a boxplot showing the area size distribution for each shape.
"""
riskified_df.boxplot(column=['area'], by=['shape'])
plt.show()


"""
2. Calculate the mean, max, and standard deviation of the area size of each color.
"""
mean_df = riskified_df.groupby(['color']).mean().reset_index()
blue_mean = 3208.131667
green_mean = 5761.119231
red_mean = 3815.871034
yellow_mean = 4538.208088

max_df = riskified_df.groupby(['color'])['area'].max().reset_index()
blue_max = 21642.4
green_max = 27759.1
red_max = 31415.9
yellow_max = 31415.9

stdev_df = riskified_df.groupby(['color']).std().reset_index()
blue_stdev = 3039.212965
green_stdev = 6695.029606
red_stdev = 5092.678377
yellow_stdev = 5352.460578


"""
3. What is the average area size of a yellow square?
"""
riskified_df[(riskified_df['shape'] == 'square') & (riskified_df['color'] == 'yellow')].mean()
avg_yellow_square = 3333.207207


"""
4. Which shape is most likely to be green?
"""
riskified_df[riskified_df['color'] == 'green'].groupby('shape')['color'].count()
common_green = 'square'


"""
5. Given the fact the the object is red, with an area size larger than 3,000 - 
what are the chances the object is a square? a triangle? a circle?
"""
big_red = riskified_df[(riskified_df['area'] > 3000) & (riskified_df['color'] == 'red')].groupby('shape')['color'].count()
(big_red / big_red.sum()) * 100
circle_pct_big_red = 16.0
square_pct_big_red = 16.8
triangle_pct_big_red = 67.2


"""
6. Write a function that calculates the side or radius of an object, depending on the shape and area of 
the object [for an Equilateral triangle - area = (side ^ 2) * sqrt(3) / 4].
"""

def compute_side_radius(df):
    if df['shape'] == 'square':
        val = math.sqrt(df['area'])
    elif df['shape'] == 'triangle':
        val = 2 * (3 ** (3/4) * math.sqrt(df['area'])) / 3
    elif df['shape'] == 'circle':
        val = math.sqrt(df['area'] / math.pi)
    return val


"""
7. Add a column to the dataset called "side" that shows the size matching the area in each row, 
round that number to the closest integer (shape side or radios).
"""
riskified_df['side'] = round(riskified_df.apply(compute_side_radius, axis=1)).astype(int)


"""
8. Draw a boxplot showing the side size distribution for each shape - what can you infer from this plot?
"""
riskified_df.boxplot(column=['side'], by=['shape'])
plt.show()
# Triangles have the longest sides, but on average the smallest area.
# Squares and triangles both have at least one outlier that approaches 0.
# The radius of the circle and side of a square are roughly the same on average.


"""
9. Make a scatter plot with "side" on the x axis, "area" on the y axis with a different color for each shape.
"""
colors = {'circle':'red', 'triangle':'blue', 'square':'green'}
fig, ax = plt.subplots()
for g in np.unique(riskified_df['shape']):
    ix = riskified_df['shape'] == g
    ax.scatter(riskified_df[ix]['side'], riskified_df[ix]['area'], c=colors[g], label=g, s=15)
ax.legend()
plt.xlabel('Length of Side')
plt.ylabel('Area of Shape')
plt.title('Area vs Side by Shape')
plt.show()


"""
10. Create a dataframe, table or list that show for each shape:
    a. The proportion of red objects within the shape
    b. The proportion of blue area out of the shape's total area (sum of square inch blue area of the 
        shape over sum of all shape size).
"""
red_shapes = riskified_df[riskified_df['color'] == 'red'].groupby('shape')['color'].count()
red_shape_prop = (red_shapes / riskified_df.groupby('shape')['color'].count()).reset_index().rename(columns={'color': 'red_objects'})

blue_area = riskified_df[riskified_df['color'] == 'blue'].groupby('shape')['area'].sum()
blue_area_prop = (blue_area / riskified_df.groupby('shape')['area'].sum()).reset_index().rename(columns={'area': 'blue_area'})

shape_df = pd.merge(red_shape_prop, blue_area_prop, on='shape')

"""
11. Create a function that calculates 10. b. for a given shape and color.
"""
def calculate_area_proportion(color, shape):
    color_area = riskified_df[(riskified_df['color'] == color) & (riskified_df['shape'] == shape)].groupby('shape')['area'].sum()
    color_area_prop = ((color_area / riskified_df[riskified_df['shape'] == shape].groupby('shape')['area'].sum())
                       .reset_index().rename(columns={'area': color + '_area'}))
    return color_area_prop


color = input('Pick a color (blue, red, yellow, or green): ')
shape = input('Pick a shape (circle, square, or triangle): ')
final_calc = calculate_area_proportion(color, shape)
final_calc

