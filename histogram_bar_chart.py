import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('histogram_bar_chart.xlsx')
bins = [0, 1, 2 , 3, 4 ,5, 6 ,7 ,8 ,9 ,10, 11]
WT_x = df['WT']
Omicron_x = df['Omicron']
plt.figure(figsize=(10,7), dpi= 200)
plt.hist([WT_x, Omicron_x], bins=bins, color=[
         'limegreen', 'violet'], edgecolor='black', alpha=0.8)
plt.xlabel('# H-bond', Fontsize=22)
plt.ylabel('Frequency', Fontsize=22)
plt.xticks(range(11))
plt.xlim([0, 11])
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.savefig('/Users/mlhossen/Desktop/Omicorn/Omicron_2/WT_RBDtrimer_w_glycans_from_6vxx_charmm-gui-4073786831_12_28_2021_100nsMD_50nsTMD/namd/H-bonds_glycan_proa.png')
