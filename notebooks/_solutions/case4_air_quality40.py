# An alternative method using `groupby` and `unstack`
data_daily.loc['2012'].groupby(['weekday', 'week'])['BETR801'].mean().unstack(level=0).boxplot();