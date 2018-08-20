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

path = ('~/desktop/rl_data.csv')
summer = pd.read_csv(path)

summer.info()
summer.head()

# We needed to replace the % symbol before we could apply any kind of numeric operations
summer_new = summer.replace({'%': ''}, regex=True)
cols = summer_new.columns.drop('school')

# Convert the columns to numeric and change them to floats by div 100
summer_new[cols] = summer_new[cols].apply(pd.to_numeric, errors='coerce')
summer_new[cols] = summer_new[cols].div(100).round(2)

summer_new = summer_new.dropna().reset_index()
summer_new.drop(columns=['index'], inplace=True)
summer_new.info()
summer_new.sample(5)


# Testing the AdjustText library
# 5th plot, adjusted 2016-17 Summer HW vs. RL
plt.clf()
def plot_adjust(adjust=True):
    # Dataframes for the subplots
    passed_2016_both = summer_new[(summer_new['hw2016'] >= 0.96) & (summer_new['rl2016'] >= 0.96)]
    passed_2016_one = summer_new[((summer_new['hw2016'] >= 0.96) & (summer_new['rl2016'] < 0.96) |
                                  (summer_new['hw2016'] < 0.96) & (summer_new['rl2016'] >= 0.96))]
    failed = summer_new[(summer_new['hw2016'] < 0.96) & (summer_new['rl2016'] < 0.96)]

    # All variables for the plot
    plt.figure(figsize=(9, 7))
    plot5 = plt.subplot()
    plot5.scatter(passed_2016_both.hw2016, passed_2016_both.rl2016, s=75, c='green', label='Passed 2016\n HW & RL')
    plot5.scatter(passed_2016_one.hw2016, passed_2016_one.rl2016, s=75, c='yellow', label='Failed 2016\n HW or RL')
    plot5.scatter(failed.hw2016, failed.rl2016, s=75, c='red', label='Failed 2016 Both')

    # Adjust size of plot and add legend to the right side
    box = plot5.get_position()
    plot5.set_position([box.x0, box.y0, box.width * 0.9, box.height])
    # leg = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, frameon=True, labelspacing=1.5)
    leg = plt.legend(loc='best', fancybox=True, frameon=True, labelspacing=1.5)
    leg.get_frame().set_edgecolor('black')

    title = plt.title("Summer HW 2016-17 vs Summer RL 2016-17", fontsize=20, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.xlabel("Summer HW 2016-17")
    plt.ylabel("Summer RL 2016-17")
    plt.ylim(.74,1)
    plt.xlim(.74,1)
    plot5.spines['right'].set_visible(False)
    plot5.spines['top'].set_visible(False)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()])

    # Adjust text variables
    texts = []
    for x,y,s in zip(summer_new['hw2016'], summer_new['rl2016'], summer_new['school']):
        texts.append(plt.text(x,y,s, size=10))
    if adjust:
        adjust_text(texts, arrowprops=dict(arrowstyle="-", color='k', lw=0.6), save_steps=False)
    plt.savefig('/users/ghodgson/desktop/graphs/summer_hw_rl_2016_17_adjusted.png')

plot_adjust()
plt.show()

# Testing the AdjustText library
# 6th Plot, Adjusted 2017-18 Summer HW vs. RL
plt.clf()
def plot_adjust(adjust=True):
    # Dataframes for the subplots
    passed_2017_both = summer_new[(summer_new['hw2017'] >= 0.96) & (summer_new['rl2017'] >= 0.96)]
    passed_2017_one = summer_new[((summer_new['hw2017'] >= 0.96) & (summer_new['rl2017'] < 0.96) |
                                  (summer_new['hw2017'] < 0.96) & (summer_new['rl2017'] >= 0.96))]
    failed = summer_new[(summer_new['hw2017'] < 0.96) & (summer_new['rl2017'] < 0.96)]

    # All variables for the plot
    plt.figure(figsize=(9, 7))
    plot6 = plt.subplot()
    plot6.scatter(passed_2017_both.hw2017, passed_2017_both.rl2017, s=75, c='green', label='Passed 2017\n HW & RL')
    plot6.scatter(passed_2017_one.hw2017, passed_2017_one.rl2017, s=75, c='yellow', label='Failed 2017\n HW or RL')
    plot6.scatter(failed.hw2017, failed.rl2017, s=75, c='red', label='Failed 2017 Both')

    # Adjust size of plot and add legend to the right side
    box = plot6.get_position()
    plot6.set_position([box.x0, box.y0, box.width * 0.9, box.height])
    # leg = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, frameon=True, labelspacing=1.5)
    leg = plt.legend(loc='best', fancybox=True, frameon=True, labelspacing=1.5)
    leg.get_frame().set_edgecolor('black')

    title = plt.title("Summer HW 2017-18 vs Summer RL 2017-18", fontsize=20, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.xlabel("Summer HW 2017-18")
    plt.ylabel("Summer RL 2017-18")
    plt.ylim(.75,1)
    plt.xlim(.75,1)
    plot6.spines['right'].set_visible(False)
    plot6.spines['top'].set_visible(False)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()])

    # Adjust text variables
    texts = []
    for x,y,s in zip(summer_new['hw2017'], summer_new['rl2017'], summer_new['school']):
        texts.append(plt.text(x,y,s, size=10))
    if adjust:
        adjust_text(texts, arrowprops=dict(arrowstyle="-", color='k', lw=0.6), save_steps=False)
    plt.savefig('/users/ghodgson/desktop/graphs/summer_hw_rl_2017_18_adjusted.png')

plot_adjust()
plt.show()


# Testing the AdjustText library
# 7th Plot, Adjusted 2016-17 HW vs. 2017-18 HW
plt.clf()
def plot_adjust(adjust=True):
    # Dataframes for the subplots
    passed_2017 = summer_new[summer_new['hw2017'] >= 0.96]
    pass_fail = summer_new[(summer_new['hw2017'] < 0.96) & (summer_new['hw2016'] >= 0.96)]
    failed = summer_new[(summer_new['hw2017'] < 0.96) & (summer_new['hw2016'] < 0.96)]

    # All variables for the plot
    plt.figure(figsize=(9, 7))
    plot7 = plt.subplot()
    plot7.scatter(passed_2017.hw2016, passed_2017.hw2017, s=75, c='green', label='Passed 2017 HW')
    plot7.scatter(pass_fail.hw2016, pass_fail.hw2017, s=75, c='yellow', label='Failed 2017 HW,\n Passed 2016 HW')
    plot7.scatter(failed.hw2016, failed.hw2017, s=75, c='red', label='Failed 2017 HW,\n Failed 2016 HW')

    # Adjust size of plot and add legend to the right side
    box = plot7.get_position()
    plot7.set_position([box.x0, box.y0, box.width * 0.85, box.height])
    # leg = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, frameon=True, labelspacing=1.5)
    leg = plt.legend(loc='best', fancybox=True, frameon=True, labelspacing=1.5)
    leg.get_frame().set_edgecolor('black')

    title = plt.title("Summer HW 2016-17 vs Summer HW 2017-18", fontsize=20, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.xlabel("Summer HW 2016-17")
    plt.ylabel("Summer HW 2017-18")
    plt.ylim(.7,1)
    plt.xlim(.7,1)
    plot7.spines['right'].set_visible(False)
    plot7.spines['top'].set_visible(False)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()])

    # Adjust text variables
    texts = []
    for x,y,s in zip(summer_new['hw2016'], summer_new['hw2017'], summer_new['school']):
        texts.append(plt.text(x,y,s, size=10))
    if adjust:
        adjust_text(texts, arrowprops=dict(arrowstyle="-", color='k', lw=0.6), save_steps=False)
    plt.savefig('/users/ghodgson/desktop/graphs/summer_hw_comparison_16-17_17-18_adjusted.png')

plot_adjust()
plt.show()


# Testing the AdjustText library
# 8th Plot, Adjusted 2016-17 RL vs. 2017-18 RL
plt.clf()
def plot_adjust(adjust=True):
    # Dataframes for the subplots
    passed_2017 = summer_new[summer_new['rl2017'] >= 0.96]
    pass_fail = summer_new[(summer_new['rl2017'] < 0.96) & (summer_new['rl2016'] >= 0.96)]
    failed = summer_new[(summer_new['rl2017'] < 0.96) & (summer_new['rl2016'] < 0.96)]

    # All variables for the plot
    fig = plt.figure(figsize=(9, 7))
    plot8 = fig.add_subplot(111)
    plot8.scatter(passed_2017.rl2016, passed_2017.rl2017, s=75, c='green', label='Passed 2017 RL')
    plot8.scatter(pass_fail.rl2016, pass_fail.rl2017, s=75, c='yellow', label='Failed 2017 RL,\n Passed 2016 RL')
    plot8.scatter(failed.rl2016, failed.rl2017, s=75, c='red', label='Failed 2017 RL,\n Failed 2016 RL')

    # Adjust size of plot and add legend to the right side
    box = plot8.get_position()
    plot8.set_position([box.x0, box.y0, box.width * 0.85, box.height])
    # leg = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, frameon=True, labelspacing=1.5)
    leg = plt.legend(loc='best', fancybox=True, frameon=True, labelspacing=1.5)
    leg.get_frame().set_edgecolor('black')

    title = plt.title("Summer RL 2016-17 vs Summer RL 2017-18", fontsize=20, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.xlabel("Summer RL 2016-17", fontname='Helvetica')
    plt.ylabel("Summer RL 2017-18")
    plt.ylim(.7,1)
    plt.xlim(.7,1)
    plot8.spines['right'].set_visible(False)
    plot8.spines['top'].set_visible(False)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()])

    # Adjust text variables
    texts = []
    for x,y,s in zip(summer_new['rl2016'], summer_new['rl2017'], summer_new['school']):
        texts.append(plt.text(x,y,s, size=10))
    if adjust:
        adjust_text(texts, arrowprops=dict(arrowstyle="-", color='k', lw=0.6), save_steps=False)
    plt.savefig('/users/ghodgson/desktop/graphs/summer_rl_comparison_16-17_17-18_adjusted.png')

plot_adjust()
plt.show()




# Test plot 3 with arrows to not overlap text
# This did not have the expected results, but I can see situations where this would be useful.

# df3 = summer_new[['school', 'hw2016', 'rl2016']]
# df3_arr = df3.to_records(index=False)
# plt.title("Summer HW 2016-17 vs Summer RL 2016-17")
# plt.xlabel("Summer HW 2016-17")
# plt.ylabel("Summer RL 2016-17")
# plt.ylim(.7,1)
# plt.xlim(.7,1)
# plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
# plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()])
# plt.clf()
#
# def getKey(item):
#     return item[2]
# df3_arr = sorted(df3_arr, key=getKey)
#
# text = [x for (x,y,z) in df3_arr]
# eucs = [y for (x,y,z) in df3_arr]
# covers = [z for (x,y,z) in df3_arr]
#
# plot3 = plt.scatter(eucs, covers, color="green")
#
# txt_height = 0.025*(plt.ylim()[1] - plt.ylim()[0])
# txt_width = 0.025*(plt.xlim()[1] - plt.xlim()[0])
#
# text_positions = get_text_positions(text, eucs, covers, txt_width, txt_height)
#
# text_plotter(text, eucs, covers, text_positions, txt_width, txt_height)
#
#
# # Functions used to help text not overlap
# import sys
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
#
# def get_text_positions(text, x_data, y_data, txt_width, txt_height):
#     a = zip(y_data, x_data)
#     text_positions = list(y_data)
#     for index, (y, x) in enumerate(a):
#         local_text_positions = [i for i in a if i[0] > (y - txt_height)
#                             and (abs(i[1] - x) < txt_width * 2) and i != (y,x)]
#         if local_text_positions:
#             sorted_ltp = sorted(local_text_positions)
#             if abs(sorted_ltp[0][0] - y) < txt_height: #True == collision
#                 differ = np.diff(sorted_ltp, axis=0)
#                 a[index] = (sorted_ltp[-1][0] + txt_height, a[index][1])
#                 text_positions[index] = sorted_ltp[-1][0] + txt_height*1.01
#                 for k, (j, m) in enumerate(differ):
#                     #j is the vertical distance between words
#                     if j > txt_height * 2: #if True then room to fit a word in
#                         a[index] = (sorted_ltp[k][0] + txt_height, a[index][1])
#                         text_positions[index] = sorted_ltp[k][0] + txt_height
#                         break
#     return text_positions
#
# def text_plotter(text, x_data, y_data, text_positions, txt_width,txt_height):
#     for z,x,y,t in zip(text, x_data, y_data, text_positions):
#         plt.annotate(str(z), xy=(x+txt_width/3, t), size=10)
#         if y != t:
#             plt.arrow(x, t ,0,y-t, color='red',alpha=0.3, width=txt_width*0.1,
#                 head_width=txt_width, head_length=txt_height*0.1,
#                 zorder=0,length_includes_head=True)
