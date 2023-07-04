#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DISCLAIMER: DATA IN THESE DEMONSTRATIONS ARE ARBITRARY. THEY DO NOT CORRESPOND TO ANY RESEARCH PAPER OR WORK.
###################################################

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

ChlamySwimmingSpeed = np.array([162,182,172,155,230,221,258]) # Chlamydomonas swimming speed measurement in um/s

# One sample t-test
ttest1Samp = sp.stats.ttest_1samp(ChlamySwimmingSpeed,popmean=150,alternative='two-sided') # alternative{‘two-sided’, ‘less’, ‘greater’}
# print(ttest1Samp)

print(ttest1Samp)
print('Probability that the Chlamy swimming speed is different from 150um/s by random chance (p_value): ',ttest1Samp.pvalue)


# In[2]:


# two - sample t-tests

# measurment of Chlamy swimming speed after a treatment
ChlamySwimmingSpeedBefore = np.array([126,182,122,155,230,221,258]) # Chlamydomonas swimming speed measurement in um/s
ChlamySwimmingSpeedAfter = np.array([156,205,158,179,210,251,208]) # Chlamydomonas swimming speed measurement in um/s

# paired
Pairedttest = sp.stats.ttest_rel(ChlamySwimmingSpeedBefore,ChlamySwimmingSpeedAfter,alternative='two-sided') # alternative{‘two-sided’, ‘less’, ‘greater’}

print('Probability that the Chlamy swimming speed shows a change after the treatment by random chance (p_value): ',Pairedttest.pvalue)


# In[3]:


# measurment of swimming speeds of two subspecies of Chlamy
ChlamySwimmingSpeed1 = np.array([126,182,122,155,230,221,258]) # Chlamydomonas species-1 swimming speed measurement in um/s
ChlamySwimmingSpeed2 = np.array([287,252,288,292,210,231,208]) # Chlamydomonas species-2 swimming speed measurement in um/s

# unpaired
UnPairedttest = sp.stats.ttest_ind(ChlamySwimmingSpeed1,ChlamySwimmingSpeed2,equal_var=True,alternative='two-sided') # If equal_var=False, perform Welch’s t-test, which does not assume equal population variance

print('Probability that the two Chlamy species shows a difference  by random chance (p_value): ',UnPairedttest.pvalue)


# In[ ]:




