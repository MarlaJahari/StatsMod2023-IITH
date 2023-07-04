#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DISCLAIMER: DATA IN THESE DEMONSTRATIONS ARE ARBITRARY. THEY DO NOT CORRESPOND TO ANY RESEARCH PAPER OR WORK.
###################################################

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

ChlamySwimmingSpeed = np.array([126,182,122,155,230,221,258,209,89,111,370]) # Chlamydomonas swimming speed measurement in um/s

print('Average speed is: ',np.mean(ChlamySwimmingSpeed),'um/s')
print('Standard deviation in speed is: ',np.std(ChlamySwimmingSpeed),'um/s')

# print(sp.stats.skew(ChlamySwimmingSpeed))
# print(sp.stats.kurtosis(ChlamySwimmingSpeed))


# In[3]:


# Correlation

ChlamySpeed = np.array([126,182,122,155,30]) # Chlamydomonas swimming speed measurement in um/s
ChlamyBeatFreq = np.array([62,82,55,65,98]) # flagellar beating frequency in Hz

plt.plot(ChlamyBeatFreq,ChlamySpeed,'o')
plt.show()

pearsonr = sp.stats.pearsonr(ChlamyBeatFreq,ChlamySpeed)
print('Pearson correlation coefficient: ', pearsonr.statistic, ' with p-value = ',pearsonr.pvalue)

spearmanr = sp.stats.spearmanr(ChlamyBeatFreq,ChlamySpeed)
print('Spearman correlation coefficient with p-value = ',spearmanr.pvalue)


# In[ ]:




