#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt



# The samples are independent.
# Each sample is from a normally distributed population.
# The population standard deviations of the groups are all equal. This property is known as homoscedasticity.


SwimmingSpeedChlamy1 = np.array([126,182,122,155,230,221,258]) # Chlamydomonas swimming speed measurement in um/s
SwimmingSpeedChlamy2 = np.array([80,75,97,84,73,91,88]) # Chlamydomonas swimming speed measurement in um/s
SwimmingSpeedChlamy3 = np.array([151,162,134,159,172,145,155]) # Chlamydomonas swimming speed measurement in um/s
SwimmingSpeedChlamy4 = np.array([176,182,153,145,139,167,133]) # Chlamydomonas swimming speed measurement in um/s

# One way ANOVA
onewayANOVA = sp.stats.f_oneway(SwimmingSpeedChlamy1, SwimmingSpeedChlamy2, SwimmingSpeedChlamy3, SwimmingSpeedChlamy4)
print('Probability that the swimming speeds of different Chlamy are different from 100um/s by random chance (p_value): ',onewayANOVA.pvalue)


# In[3]:


# non parametric when any of the assumptions are not met
kruskal = sp.stats.kruskal(SwimmingSpeedChlamy1, SwimmingSpeedChlamy2, SwimmingSpeedChlamy3, SwimmingSpeedChlamy4)
print('Probability that the swimming speeds of different Chlamy are different from 100um/s by random chance (p_value): ',kruskal.pvalue)


# In[4]:


# post-hoc analysis
fig, ax = plt.subplots(1, 1)
ax.boxplot([SwimmingSpeedChlamy1, SwimmingSpeedChlamy2, SwimmingSpeedChlamy3, SwimmingSpeedChlamy4])
ax.set_xticklabels(["sp1", "sp2", "sp3", "sp4"])
ax.set_ylabel("mean")
plt.show()


# In[5]:


res = sp.stats.tukey_hsd(SwimmingSpeedChlamy1, SwimmingSpeedChlamy2, SwimmingSpeedChlamy3, SwimmingSpeedChlamy4)
print(res)


# In[ ]:




