
# coding: utf-8

# # Moments: Mean, Variance, Skew, Kurtosis

# Create a roughly normal-distributed random set of data:

# In[6]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(10, 0.5, 10000)

plt.hist(vals, 50)
plt.show()


# The first moment is the mean; this data should average out to about 0:

# In[7]:

np.mean(vals)


# The second moment is the variance:

# In[8]:

np.var(vals)


# The third moment is skew - since our data is nicely centered around 0, it should be almost 0:

# In[9]:

import scipy.stats as sp
sp.skew(vals)


# The fourth moment is "kurtosis", which describes the shape of the tail. For a normal distribution, this is 0:

# In[10]:

sp.kurtosis(vals)


# ## Activity

# Understanding skew: change the normal distribution to be centered around 10 instead of 0, and see what effect that has on the moments.
# 
# The skew is still near zero; skew is associated with the shape of the distribution, not its actual offset in X.

# In[11]:

print "done"


# In[ ]:



