import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import matplotlib as mpl
from datetime import datetime, timedelta
from palettable.cartocolors.qualitative import Safe_6
from matplotlib.colors import ListedColormap

new_data_day = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

combined_totals = pd.read_csv('./ytd_totals.csv')
combined_totals = combined_totals.set_index('Agency')

df_provinces = combined_totals.loc[combined_totals.index != 'Canada']
df_national = combined_totals.loc['Canada'].to_frame().transpose()

fig, ax = plt.subplots(1,1,figsize=(10,4))
df_provinces.plot(kind='bar',ax=ax,cmap=Safe_6.mpl_colormap,zorder=2)
ax.grid(True)
ax.set_title('Year-To-Date Smoke Cover by Province',fontsize=18)

ax.set_ylabel('Smoke (km²)',fontsize=14)
ax.set_xlabel('Province',fontsize=14)
plt.text(.06, .98, f'Current as of {new_data_day}' '\n' 'Data Courtesy of ECCC/NOAA OSPO', ha='left', va='top', transform=ax.transAxes)
plt.legend(loc='lower center',fontsize=14,bbox_to_anchor=(0.5,-0.05),ncol=6)

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),
          fancybox=True, ncol=6)
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

# fig2, ax2 = plt.subplots(1,1,figsize=(12,8))
# df_national.plot(kind='bar',ax=ax2,colormap='tab10')
# ax2.set_ylabel('Smoke (km²)',fontsize=14)
# ax2.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))