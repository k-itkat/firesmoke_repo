import pandas as pd
from datetime import datetime, timedelta

'''
downloads smoke cover data from Jan 1st, 2020, until current day
'''
new_data_day = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
link = 'https://cwfis.cfs.nrcan.gc.ca/maps/fm3?type=rpt&'
dr = pd.date_range(start='1/1/2020', end=new_data_day)
yearly_totals = {}

print(new_data_day)

cutoff_month = int(str(new_data_day)[5:7])
cutoff_day = int(str(new_data_day)[8:10])

for i in dr:
    dt = (i.date())
    dt_str = str(dt)
    year = dt_str[0:4]
    if dt > datetime(dt.year, cutoff_month, cutoff_day).date():
        continue
    lt = link[0:48]+f'year={year}'+'&month='+dt_str[6]+'&day='+dt_str[8:10]
    data = pd.read_html(lt)[0]
    data = data.set_index('Agency')['Smoke (km2)']
    if year not in yearly_totals:
        yearly_totals[year] = pd.Series(dtype=float)     
    yearly_totals[year] = yearly_totals[year].add(data,fill_value=0)

combined_totals = pd.DataFrame(yearly_totals)
combined_totals.to_csv('./ytd_totals.csv')