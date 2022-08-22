#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:14:12 2021

@author: mlhossen
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#x, y = np.loadtxt("3_combination_3_1_3_2.txt",unpack=True)
#x, y = np.loadtxt("/Users/mlhossen/Desktop/moon_chap/3_charmm-gui-3461161253/namd/3_combination_3_1_3_2.txt",unpack=True)

with open("/Users/mlhossen/Desktop/moon_chap/dihedrals_calculation/combination_of_comp_1_2_3_4_for_2DHistogram.dat", "r") as f:

    #x = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    y8 = []
    for line in f:
        if not line.strip() or line.startswith('@') or line.startswith('#'):
            continue
        row = line.split()
        #x.append(float(row[0]))
        y1.append(float(row[1]))
        y2.append(float(row[2]))
        y3.append(float(row[3]))
        y4.append(float(row[4]))
        y5.append(float(row[5]))
        y6.append(float(row[6]))
        y7.append(float(row[7]))
        y8.append(float(row[8]))

#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharex='col', sharey='row', gridspec_kw={'hspace': 0, 'wspace': 0})
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(nrows=2, ncols=2, figsize = (10,10), gridspec_kw={'hspace': 0.01, 'wspace': 0.008})

#fig.subplots_adjust(wspace=0.01)
ax1.hist2d(y1, y2, 30, cmap=plt.cm.coolwarm, vmin=0, vmax=30)
ax2.hist2d(y3, y4, 30, cmap=plt.cm.coolwarm, vmin=0, vmax=30)
ax3.hist2d(y5, y6, 30, cmap=plt.cm.coolwarm, vmin=0, vmax=30)
ax4.hist2d(y7, y8, 30, cmap=plt.cm.coolwarm, vmin=0, vmax=30)

ax1.legend()
ax1.yaxis.set_tick_params(labelsize=22)
ax1.set_ylabel(r"$\psi$" '(degree)', Fontsize=22)
#plt.yticks([-150, -75, 0, 75, 150], ['-150', '-75', '0', '75', '150'])

ax2.legend()
#plt.margins(x=0)
ax2.yaxis.set_tick_params(labelsize=0)
#ax2.yaxis.set_ticks_position('right')


ax3.legend()
ax3.xaxis.set_tick_params(labelsize=22)
ax3.yaxis.set_tick_params(labelsize=22)
ax3.set_xlabel(r"$\phi$" '(degree)', Fontsize=22)
ax3.set_ylabel(r"$\psi$" '(degree)', Fontsize=22)

ax4.legend()
ax4.xaxis.set_tick_params(labelsize=22)
ax4.yaxis.set_tick_params(labelsize=0)
ax4.set_xlabel(r"$\phi$" '(degree)', Fontsize=22)
#ax4.yaxis.set_ticks_position('right')

plt.tight_layout()

im = plt.gca().get_children()[0]
cax = fig.add_axes([0.925,0.12655,0.03,0.755]) 
cbar = fig.colorbar(im, cax=cax)
cbar.ax.tick_params(labelsize=22)
plt.savefig("/Users/mlhossen/Desktop/moon_chap/dihedrals_calculation/combination_of_all_4_compound.png", dpi=1200)
plt.show()
