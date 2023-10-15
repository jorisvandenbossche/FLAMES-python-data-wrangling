# Groupby wise
df2011 = data.loc['2011']
df2011.groupby(data.index.isocalendar().week)[['BETN029', 'BETR801']].quantile(0.95).plot()