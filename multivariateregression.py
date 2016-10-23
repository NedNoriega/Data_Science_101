
# coding: utf-8

# # Multivariate Regression

# Let's grab a small little data set of Blue Book car values:

# In[12]:

import pandas as pd

df = pd.read_excel('C:/Users/noriegn/Desktop/test.xlsx')


# In[15]:

df.head(10)


# We can use pandas to split up this matrix into the feature vectors we're interested in, and the value we're trying to predict.
# 
# Note how we use pandas.Categorical to convert textual category data (model name) into an ordinal number that we can work with.

# In[3]:

import statsmodels.api as sm

df['Model_ord'] = pd.Categorical(df.Model).codes
X = df[['Mileage', 'Model_ord', 'Doors']]
y = df[['Price']]

X1 = sm.add_constant(X)
est = sm.OLS(y, X1).fit()

est.summary()

The table of coefficients above gives us the values to plug into an equation of form:
    B0 + B1 * Mileage + B2 * model_ord + B3 * doors
    
But in this example, it's pretty clear that mileage is more important than anything based on the std err's.

Could we have figured that out earlier?
# In[4]:

y.groupby(df.Doors).mean()


# Surprisingly, more doors does not mean a higher price! So it's not surprising that it's pretty useless as a predictor here. This is a very small data set however, so we can't really read much meaning into it.

# ## Activity

# Mess around with the fake input data, and see if you can create a measurable influence of number of doors on price. Have some fun with it - why stop at 4 doors?

# In[16]:

print "Remember to substitude the blackslash for a forwardslash in the path. df.head(number of rows starting at 0)"


# In[ ]:



