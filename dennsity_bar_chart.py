import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set_style("white")

# Import data
df = pd.read_excel('WT_Omicron_together_1.xlsx')
x1 = df['WT']
x2 = df['Omicron']

# Plot
kwargs = dict(hist_kws={'alpha':.5}, kde_kws={'linewidth':3})

plt.figure(figsize=(10,7), dpi= 200)
sns.distplot(x1, color="mediumpurple", label="WT", **kwargs)
sns.distplot(x2, color="lightgreen", label="Omicron", **kwargs)
plt.xlim(-0.02,0.12)
plt.xlabel('# H-bond', Fontsize=22)
plt.ylabel('Frequency', Fontsize=22)
plt.xticks([-0.02, 0.00, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12], ['-2.0', '0.0', '2.0', '4.0', '6.0', '8.0', '10.0', '12.0'])#ticks label change
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend();
plt.savefig('/Users/mlhossen/Desktop/Omicorn/Omicron_2/WT_RBDtrimer_w_glycans_from_6vxx_charmm-gui-4073786831_12_28_2021_100nsMD_50nsTMD/namd/H-bonds_glycan_proa.png')
