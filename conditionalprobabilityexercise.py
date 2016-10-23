
# coding: utf-8

# # Conditional Probability Activity & Exercise

# Below is some code to create some fake data on how much stuff people purchase given their age range.
# 
# It generates 100,000 random "people" and randomly assigns them as being in their 20's, 30's, 40's, 50's, 60's, or 70's.
# 
# It then assigns a lower probability for young people to buy stuff.
# 
# In the end, we have two Python dictionaries:
# 
# "totals" contains the total number of people in each age group.
# "purchases" contains the total number of things purchased by people in each age group.
# The grand total of purchases is in totalPurchases, and we know the total number of people is 100,000.
# 
# Let's run it and have a look:

# In[4]:

from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0
for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = float(ageDecade) / 100.0
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1


# In[5]:

totals


# In[6]:

purchases


# In[7]:

totalPurchases


# Let's play with conditional probability.
# 
# First let's compute P(E|F), where E is "purchase" and F is "you're in your 30's". The probability of someone in their 30's buying something is just the percentage of how many 30-year-olds bought something:

# In[8]:

PEF = float(purchases[30]) / float(totals[30])
print "P(purchase | 30s): ", PEF


# P(F) is just the probability of being 30 in this data set:

# In[9]:

PF = float(totals[30]) / 100000.0
print "P(30's): ", PF


# And P(E) is the overall probability of buying something, regardless of your age:

# In[10]:

PE = float(totalPurchases) / 100000.0
print "P(Purchase):", PE


# If E and F were independent, then we would expect P(E | F) to be about the same as P(E). But they're not; PE is 0.45, and P(E|F) is 0.3. So, that tells us that E and F are dependent (which we know they are in this example.)
# 
# What is P(E)P(F)?

# In[11]:

print "P(30's)P(Purchase)", PE * PF


# P(E,F) is different from P(E|F). P(E,F) would be the probability of both being in your 30's and buying something, out of the total population - not just the population of people in their 30's:

# In[12]:

print "P(30's, Purchase)", float(purchases[30]) / 100000.0


# P(E,F) = P(E)P(F), and they are pretty close in this example. But because E and F are actually dependent on each other, and the randomness of the data we're working with, it's not quite the same.
# 
# We can also check that P(E|F) = P(E,F)/P(F) and sure enough, it is:

# In[13]:

(float(purchases[30]) / 100000.0) / PF


# ## Your Assignment

# Modify the code above such that the purchase probability does NOT vary with age, making E and F actually independent.
# 
# Then, confirm that P(E|F) is about the same as P(E), showing that the conditional probability of purchase for a given age is not any different than the a-priori probability of purchase regardless of age.
# 

# In[76]:

from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0
for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = 0.4
    totals[ageDecade] += 1
    if (random.normal() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1


# In[77]:

totals


# In[78]:

purchases


# In[79]:

totalPurchases


# In[80]:

PEF = float(purchases[30]) / float(totals[30])
PE = float(totalPurchases) / 100000.0

print "If ", PEF ,"equals to ", PE ,", then E and F are independent."


# In[75]:

print "Difficult to understand how to distribute evenly the purchases across all age decades."


# In[81]:

print "The key concept was to assign purchaseProbability = constant value"


# In[ ]:



