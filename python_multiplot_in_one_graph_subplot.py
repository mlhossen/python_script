#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 20:56:15 2021

@author: mlhossen
"""

import pandas as pd
from matplotlib import pyplot as plt

#plt.style.use('seaborn')

with open("/Users/mlhossen/Desktop/moon_chap/2_charmm-gui-3434013786/namd/2_head_and_tail_moon.dat", "r") as f:

    x = []
    y1 = []
    y2 = []
    for line in f:
        if not line.strip() or line.startswith('@') or line.startswith('#'):
            continue
        row = line.split()
        x.append(float(row[0]))
        y1.append(float(row[1]))
        y2.append(float(row[2]))
        
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)

ax1.plot(x, y1)
ax2.plot(x, y2)

ax1.legend()
#ax1.set_xlabel("Time(ns)")
ax1.yaxis.set_tick_params(labelsize=20)
ax1.set_ylabel(r"$\phi$" '(degree)', Fontsize=20)

ax2.legend()
ax2.set_xlabel("Time(ns)", Fontsize=20)
ax2.xaxis.set_tick_params(labelsize=20)
ax2.yaxis.set_tick_params(labelsize=20)
plt.margins(x=0)
plt.xticks([0, 100, 200, 300, 400, 500], ['0', '20', '40', '60', '80', '100'])
ax2.set_ylabel(r"$\psi$" '(degree)', Fontsize=20)

plt.tight_layout()
plt.savefig("/Users/mlhossen/Desktop/compound_2.png", dpi=1200)
plt.show()
