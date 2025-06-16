import pandas as pd
from datetime import datetime, timedelta

new_data_day = str((datetime.now() - timedelta(1)).strftime('%Y-%m-%d'))
print(new_data_day)
link = 'https://cwfis.cfs.nrcan.gc.ca/maps/fm3?type=rpt&'

lt = link[0:48]+'year='+new_data_day[0:4]+'&month='+new_data_day[6]+'&day='+new_data_day[8:10]

combined_totals = pd.read_csv('./ytd_totals.csv')
combined_totals = combined_totals.set_index('Agency')
#print(combined_totals)
data = pd.read_html(lt)[0]
data = data.set_index('Agency')['Smoke (km2)']
#print(data)

combined_totals['2025'] = combined_totals['2025']+data
# combined_totals.to_csv('./ytd_totals')
