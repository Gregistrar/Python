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

path = ('~/desktop/absence_tardy_data.csv')
culture = pd.read_csv(path)

culture.info()
culture.head()

# We needed to replace the % symbol before we could apply any kind of numeric operations
culture_new = culture.replace({'%': ''}, regex=True)
cols = culture_new.columns.drop('school')

# Convert the columns to numeric and change them to floats by div 100
culture_new[cols] = culture_new[cols].apply(pd.to_numeric, errors='coerce')
culture_new[cols] = culture_new[cols].div(100).round(4)

culture_new = culture_new.dropna().reset_index()
culture_new.drop(columns=['index'], inplace=True)
culture_new.info()
culture_new.sample(5)


# Testing the AdjustText library
# 1st plot, adjusted text 2017-18 Absences vs. Tardies (Unexcused)
plt.clf()
def plot_adjust(adjust=True):
    # Dataframes for the subplots
    passed_2017_both = culture_new[
        (culture_new['absences_unexcused_2017'] >= 0.97) & (culture_new['tardies_unexcused_2017'] >= 0.96)]

    passed_2017_one = culture_new[
        ((culture_new['absences_unexcused_2017'] >= 0.97) & (culture_new['tardies_unexcused_2017'] < 0.96) |
         (culture_new['absences_unexcused_2017'] < 0.97) & (culture_new['tardies_unexcused_2017'] >= 0.96))]

    failed = culture_new[
        (culture_new['absences_unexcused_2017'] < 0.97) & (culture_new['tardies_unexcused_2017'] < 0.96)]

    # All variables for the plot
    plt.figure(figsize=(9, 7))
    plot1 = plt.subplot()
    plot1.scatter(passed_2017_both.absences_unexcused_2017, passed_2017_both.tardies_unexcused_2017, s=75, c='#f7910b', label='Met 2017 Absence\n& Tardy Goals')
    plot1.scatter(passed_2017_one.absences_unexcused_2017, passed_2017_one.tardies_unexcused_2017, s=75, c='#f7910b', label='Met One Culture\nGoal in 2017')
    plot1.scatter(failed.absences_unexcused_2017, failed.tardies_unexcused_2017, s=75, c='#f7910b', label='Did Not Meet\nEither Culture Goal')

    # Adjust size of plot and add legend to the right side
    box = plot1.get_position()
    plot1.set_position([box.x0, box.y0, box.width, box.height])
    #leg = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, frameon=True, labelspacing=1.5)
    leg = plt.legend(loc='best', fancybox=True, frameon=True, labelspacing=1.5)
    leg.get_frame().set_edgecolor('black')

    title = plt.title("2017-18 Unexcused Absences vs. Unexcused Tardies", fontsize=20, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.xlabel("2017-18 Unexcused Absences")
    plt.ylabel("2017-18 Unexcused Tardies")
    plt.ylim(.93,1)
    plt.xlim(.93,1)
    plot1.spines['right'].set_visible(False)
    plot1.spines['top'].set_visible(False)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()])

    # Adjust text variables
    texts = []
    for x,y,s in zip(culture_new['absences_unexcused_2017'], culture_new['tardies_unexcused_2017'], culture_new['school']):
        texts.append(plt.text(x,y,s, size=10))
    if adjust:
        adjust_text(texts, arrowprops=dict(arrowstyle="-", color='k', lw=0.6), save_steps=False)
    plt.savefig('/users/ghodgson/desktop/graphs/culture/2017_absence_tardy_unexcused_adjusted.png')

plot_adjust()
plt.show()


# 2nd plot, adjusted text 2017-18 Absences vs. Tardies (All)
plt.clf()
def plot_adjust(adjust=True):
    # Dataframes for the subplots
    passed_2017_both = culture_new[(culture_new['absences_all_2017'] >= 0.97) & (culture_new['tardies_all_2017'] >= 0.96)]

    passed_2017_one = culture_new[((culture_new['absences_all_2017'] >= 0.97) & (culture_new['tardies_all_2017'] < 0.96) |
                                  (culture_new['absences_all_2017'] < 0.97) & (culture_new['tardies_all_2017'] >= 0.96))]

    failed = culture_new[(culture_new['absences_all_2017'] < 0.97) & (culture_new['tardies_all_2017'] < 0.96)]

    # All variables for the plot
    plt.figure(figsize=(9, 7))
    plot2 = plt.subplot()
    plot2.scatter(passed_2017_both.absences_all_2017, passed_2017_both.tardies_all_2017, s=75, c='#f7910b', label='Met 2017 Absence\n& Tardy Goals')
    plot2.scatter(passed_2017_one.absences_all_2017, passed_2017_one.tardies_all_2017, s=75, c='#f7910b', label='Met One Culture\nGoal in 2017')
    plot2.scatter(failed.absences_all_2017, failed.tardies_all_2017, s=75, c='#f7910b', label='Did Not Meet\nEither Culture Goal')

    # Adjust size of plot and add legend to the right side
    box = plot2.get_position()
    plot2.set_position([box.x0, box.y0, box.width, box.height])
    #leg = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, frameon=True, labelspacing=1.5)
    #leg = plt.legend(loc='best', fancybox=True, frameon=True, labelspacing=1.5)
    #leg.get_frame().set_edgecolor('black')

    title = plt.title("2017-18 All Absences vs. All Tardies (Includes Excused)", fontsize=20, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.xlabel("2017-18 All Absences")
    plt.ylabel("2017-18 All Tardies")
    plt.ylim(.93,1)
    plt.xlim(.93,1)
    plot2.spines['right'].set_visible(False)
    plot2.spines['top'].set_visible(False)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()])

    # Adjust text variables
    texts = []
    for x,y,s in zip(culture_new['absences_all_2017'], culture_new['tardies_all_2017'], culture_new['school']):
        texts.append(plt.text(x,y,s, size=10))
    if adjust:
        adjust_text(texts, arrowprops=dict(arrowstyle="-", color='k', lw=0.6), save_steps=False)
    plt.savefig('/users/ghodgson/desktop/graphs/culture/2017_absence_tardy_all_adjusted.png')

plot_adjust()
plt.show()


# 3rd plot, adjusted text 2017-18 First 30 Days Absences vs. Tardies (Unexcused)
plt.clf()
def plot_adjust(adjust=True):
    # Dataframes for the subplots
    passed_2017_both = culture_new[(culture_new['first30_absences_unexcused_2017'] >= 0.97) & (culture_new['first30_tardies_unexcused_2017'] >= 0.96)]

    passed_2017_one = culture_new[((culture_new['first30_absences_unexcused_2017'] >= 0.97) & (culture_new['first30_tardies_unexcused_2017'] < 0.96) |
                                  (culture_new['first30_absences_unexcused_2017'] < 0.97) & (culture_new['first30_tardies_unexcused_2017'] >= 0.96))]

    failed = culture_new[(culture_new['first30_absences_unexcused_2017'] < 0.97) & (culture_new['first30_tardies_unexcused_2017'] < 0.96)]

    # All variables for the plot
    plt.figure(figsize=(9, 7))
    plot3 = plt.subplot()
    plot3.scatter(passed_2017_both.first30_absences_unexcused_2017, passed_2017_both.first30_tardies_unexcused_2017, s=75, c='#34a43e', label='Met 2017 Absence\n& Tardy Goals')
    plot3.scatter(passed_2017_one.first30_absences_unexcused_2017, passed_2017_one.first30_tardies_unexcused_2017, s=75, c='#ffd200', label='Met One Culture\nGoal in 2017')
    plot3.scatter(failed.first30_absences_unexcused_2017, failed.first30_tardies_unexcused_2017, s=75, c='#b30000', label='Did Not Meet\nEither Culture Goal')

    # Adjust size of plot and add legend to the right side
    box = plot3.get_position()
    plot3.set_position([box.x0, box.y0, box.width, box.height])
    #leg = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, frameon=True, labelspacing=1.5)
    leg = plt.legend(loc='best', fancybox=True, frameon=True, labelspacing=1.5)
    leg.get_frame().set_edgecolor('black')

    title = plt.title("2017-18 First 30 Days - Unexcused Absences\nvs. Unexcused Tardies", fontsize=20, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.xlabel("2017-18 First 30 Days Unexcused Absences")
    plt.ylabel("2017-18 First 30 Days Unexcused Tardies")
    plt.ylim(.93,1)
    plt.xlim(.93,1)
    plot3.spines['right'].set_visible(False)
    plot3.spines['top'].set_visible(False)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()])

    # Adjust text variables
    texts = []
    for x,y,s in zip(culture_new['first30_absences_unexcused_2017'], culture_new['first30_tardies_unexcused_2017'], culture_new['school']):
        texts.append(plt.text(x,y,s, size=10))
    if adjust:
        adjust_text(texts, arrowprops=dict(arrowstyle="-", color='k', lw=0.6), save_steps=False)
    plt.savefig('/users/ghodgson/desktop/graphs/culture/2017_first30_absence_tardy_unexcused_adjusted.png')

plot_adjust()
plt.show()


# 4th plot, adjusted text 2017-18 First 30 Days Absences vs. Tardies (All)
plt.clf()
def plot_adjust(adjust=True):
    # Dataframes for the subplots
    passed_2017_both = culture_new[(culture_new['first30_absences_all_2017'] >= 0.97) & (culture_new['first30_tardies_all_2017'] >= 0.96)]

    passed_2017_one = culture_new[((culture_new['first30_absences_all_2017'] >= 0.97) & (culture_new['first30_tardies_all_2017'] < 0.96) |
                                  (culture_new['first30_absences_all_2017'] < 0.97) & (culture_new['first30_tardies_all_2017'] >= 0.96))]

    failed = culture_new[(culture_new['first30_absences_all_2017'] < 0.97) & (culture_new['first30_tardies_all_2017'] < 0.96)]

    # All variables for the plot
    plt.figure(figsize=(9, 7))
    plot4 = plt.subplot()
    plot4.scatter(passed_2017_both.first30_absences_all_2017, passed_2017_both.first30_tardies_all_2017, s=75, c='#f7910b', label='Met 2017 Absence\n& Tardy Goals')
    plot4.scatter(passed_2017_one.first30_absences_all_2017, passed_2017_one.first30_tardies_all_2017, s=75, c='#f7910b', label='Met One Culture\nGoal in 2017')
    plot4.scatter(failed.first30_absences_all_2017, failed.first30_tardies_all_2017, s=75, c='#f7910b', label='Did Not Meet\nEither Culture Goal')

    # Adjust size of plot and add legend to the right side
    box = plot4.get_position()
    plot4.set_position([box.x0, box.y0, box.width, box.height])
    #leg = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, frameon=True, labelspacing=1.5)
    #leg = plt.legend(loc='best', fancybox=True, frameon=True, labelspacing=1.5)
    #leg.get_frame().set_edgecolor('black')

    title = plt.title("2017-18 First 30 Days - All Absences\nvs. All Tardies (Includes Excused)", fontsize=20, fontweight='bold')
    title.set_position([.5, 1.02])
    plt.xlabel("2017-18 First 30 Days All Absences")
    plt.ylabel("2017-18 First 30 Days All Tardies")
    plt.ylim(.925,1)
    plt.xlim(.93,1)
    plot4.spines['right'].set_visible(False)
    plot4.spines['top'].set_visible(False)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.gca().set_xticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_xticks()])

    # Adjust text variables
    texts = []
    for x,y,s in zip(culture_new['first30_absences_all_2017'], culture_new['first30_tardies_all_2017'], culture_new['school']):
        texts.append(plt.text(x,y,s, size=10))
    if adjust:
        adjust_text(texts, arrowprops=dict(arrowstyle="-", color='k', lw=0.6), save_steps=False)
    plt.savefig('/users/ghodgson/desktop/graphs/culture/2017_first30_absence_tardy_all_adjusted.png')

plot_adjust()
plt.show()

