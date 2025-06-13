import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
today = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
print(today)

link = 'https://cwfis.cfs.nrcan.gc.ca/maps/fm3?type=rpt&'
lt = link[0:48]+'year='+today[0:4]+'&month='+today[6:7]+'&day='+today[8:10]

years = [2018,2019,2020,2021,2022,2023,2024,2025]

#firedata_2025 = pd.read_html(link)[0]
#firedata_2025 = pd.read_html('https://cwfis.cfs.nrcan.gc.ca/maps/fm3?type=rpt&year=2025&month=6&day=11')[0]
firedata_2025 = pd.read_html(lt)[0]
firedata_2025 = firedata_2025.set_index('Agency')
firedata_2025 = firedata_2025.drop('Cloud (%)',axis=1)

firedata_2024 = pd.read_html('https://cwfis.cfs.nrcan.gc.ca/maps/fm3?type=rpt&year=2024&month=6&day=11')[0]
firedata_2024 = firedata_2024.set_index('Agency')
firedata_2024 = firedata_2024.drop('Cloud (%)',axis=1)

firedata_2023 = pd.read_html('https://cwfis.cfs.nrcan.gc.ca/maps/fm3?type=rpt&year=2023&month=6&day=11')[0]
firedata_2023 = firedata_2023.set_index('Agency')

firedata_2025['year']=2025
firedata_2024['year']=2024

firedata_2025 = firedata_2025.rename(columns={'Smoke (km2)': 'smoke_2025'})
firedata_2024 = firedata_2024.rename(columns={'Smoke (km2)': 'smoke_2024'})
firedata_2023 = firedata_2023.rename(columns={'Smoke (km2)': 'smoke_2023'})
print(firedata_2024)
smoke = pd.concat([firedata_2025['smoke_2025'],firedata_2024['smoke_2024'],firedata_2023['smoke_2023']],axis=1)
print(smoke)
smoke.plot.bar()
plt.show()

# all_yrs = pd.concat([firedata_2024,firedata_2025],ignore_index=True)
# all_yrs = all_yrs.melt(id_vars='year',var_name='variable',value_name='value')
# print(all_yrs)

# variables = all_yrs['variable'].unique()
# print(variables)
# fig, axes = plt.subplots(2,2,figsize=(12,10),sharex=True)
# for i, var in enumerate(variables):
#     ax = axes[i]
#     subset = all_yrs[all_yrs['variable']==var]
#     #print(subset)
#     #ax = firedata_2025[var].plot.bar(ax=ax)
#     sns.barplot(data=subset,x='year', y='value',ax=ax)
# plt.show()



# fig, axes = plt.subplots(2,2,figsize=(12,10))
# axes = axes.flatten()

# print(firedata_2025)

# for i, var in enumerate(list(firedata_2025.columns.values)):
#     print(firedata_2025[var])
#     ax = axes[i]
#     ax = firedata_2025[var].plot.bar(ax=ax)
#     ax.set_title(var)