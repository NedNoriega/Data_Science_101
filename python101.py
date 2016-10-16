
# coding: utf-8

# # Python Basics

# ## Whitespace Is Important

# In[1]:

listOfNumbers = [1, 2, 3, 4, 5, 6]

for number in listOfNumbers:
    print number,
    if (number % 2 == 0):
        print "is even"
    else:
        print "is odd"
        
print "Horray! We're all done. Let's party!"
        


# ## Importing Modules

# In[6]:

import numpy as np

A = np.random.normal(65.0, 5.0, 20)
print A


# ## Lists

# In[7]:

x = [1, 2, 3, 4, 5, 6, 18, 19, 20]
print len(x)


# In[4]:

x[:3]


# In[8]:

x[3:]


# In[9]:

x[-2:]


# In[10]:

x.extend([7,8])
x


# In[11]:

x.append(9)
x


# In[12]:

y = [10, 11, 12]
listOfLists = [x, y]
listOfLists


# In[13]:

y[1]


# In[14]:

z = [3, 2, 1]
z.sort()
z


# In[15]:

z.sort(reverse=True)
z


# ## Tuples

# In[13]:

#Tuples are just immutable lists. Use () instead of []
x = (1, 2, 3)
len(x)


# In[14]:

y = (4, 5, 6)
y[2]


# In[15]:

listOfTuples = [x, y]
listOfTuples


# In[16]:

(age, income) = "32,120000".split(',')
print age
print income


# ## Dictionaries

# In[23]:

# Like a map or hash table in other languages
captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"

print captains["Voyager"]


# In[24]:

print captains.get("Enterprise")


# In[25]:

print captains.get("NX-01")


# In[27]:

for ship in captains:
    print ship + ": " + captains[ship]


# ## Functions

# In[3]:

def SquareIt(x):
    return x * x

print SquareIt(4)


# In[2]:

#You can pass functions around as parameters
def DoSomething(f, x):
    return f(x)

print DoSomething(SquareIt, 3)


# In[23]:

#Lambda functions let you inline simple functions
print DoSomething(lambda x: x * x * x, 3)


# ## Boolean Expressions

# In[24]:

print 1 == 3


# In[25]:

print (True or False)


# In[26]:

print 1 is 3


# In[27]:

if 1 is 3:
    print "How did that happen?"
elif 1 > 3:
    print "Yikes"
else:
    print "All is well with the world"


# ## Looping

# In[28]:

for x in range(10):
    print x,


# In[29]:

for x in range(10):
    if (x is 1):
        continue
    if (x > 5):
        break
    print x,


# In[30]:

x = 0
while (x < 10):
    print x,
    x += 1


# ## Activity

# Write some code that creates a list of integers, loops through each element of the list, and only prints out even numbers!

# In[4]:

for x in range(1,101):
    if (x % 3 == 0 and x % 5 == 0):
        print "fizzbuzz"
    elif (x % 3 == 0):
        print "fizz"
    elif (x % 5 == 0):
        print "buzz"
    else:
        print x

        


# In[39]:

#One of them leads to a pretty concise (and quite obscure) solution of the Fizzbuzz problem :
['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, 100)]


# In[40]:

# Another FizzBuzz solution similar to mine:
for num in xrange(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print "FizzBuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num


# In[ ]:



