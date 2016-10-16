
# coding: utf-8

# # Percentiles

# In[1]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()


# In[6]:

np.percentile(vals, 50)


# In[9]:

np.percentile(vals, 99)


# In[10]:

np.percentile(vals, 1)


# ## Activity

# Experiment with different parameters when creating the test data. What effect does it have on the percentiles?

# In[11]:

print "done"


# In[ ]:



