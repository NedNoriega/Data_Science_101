
# coding: utf-8

# # Standard Deviation and Variance

# In[9]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)

plt.hist(incomes, 50)
plt.show()


# In[10]:

incomes.std()


# In[11]:

incomes.var()


# ## Activity

# Experiment with different parameters on the normal function, and see what effect it has on the shape of the distribution. How does that new shape relate to the standard deviation and variance?

# In[12]:

print "done"


# In[ ]:



