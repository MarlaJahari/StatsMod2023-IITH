#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DISCLAIMER: DATA IN THESE DEMONSTRATIONS ARE ARBITRARY. THEY DO NOT CORRESPOND TO ANY RESEARCH PAPER OR WORK.
###################################################

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from statsmodels.stats.power import TTestIndPower


powerAnalysis = TTestIndPower()
sampleSize = powerAnalysis.solve_power(effect_size=0.2, power=0.9, alpha=0.05)
print(sampleSize)



#  TTestIndPower.solve_power(effect_size=None, nobs1=None, alpha=None, power=None, ratio=1.0, alternative='two-sided')

power = powerAnalysis.solve_power(effect_size=0.2, nobs1=100, alpha=0.05)
print(power)


# In[2]:


effectSizes = np.array([0.2, 0.5, 0.8])
sampleSizes = np.array(range(10, 500, 10))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
fig = powerAnalysis.plot_power(
    dep_var='nobs', nobs=sampleSizes,
    effect_size=effectSizes, alpha=0.05, ax=ax,
    )
plt.ylabel('Power')


# In[ ]:




