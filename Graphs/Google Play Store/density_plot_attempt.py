


# Density plot of Google Play Store installs of apps
google_installs = clean_data[['installs']]
google_installs.installs.value_counts()
google_installs.info()
google_installs['installs'] = google_installs['installs'].map(lambda x: ''.join([i for i in x if i.isdigit()]))
google_installs['installs'] = [x.replace(' ', '') for x in google_installs['installs']]
google_installs['installs'] = google_installs['installs'].apply(pd.to_numeric)

from scipy.stats import gaussian_kde
install_list = google_installs['installs'].tolist()
density = gaussian_kde(install_list)
xs = np.linspace(0, 1000000, 100)
density.covariance_factor = lambda: 1000000
density._compute_covariance()
plt.plot(xs, density(xs))


import seaborn as sns
install_list = google_installs['installs'].tolist()
install_array = np.array(install_list)
sns.set_style('whitegrid')
sns.set(color_codes=True)
sns.kdeplot(np.array(install_list), bw=.2)

sns.distplot(install_array)


sns.distplot(install_array, kde=False, rug=True)

sns.distplot(install_array, hist=True, kde=True,
             bins=int(180/10), color = 'darkblue',
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 2})
