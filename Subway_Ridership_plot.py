
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for each block of code to see what it does




# In[8]:

# Examine DataFrame
if False:
    print example_df
    
# Examine groups
if False:
    grouped_data = example_df.groupby('even')
    # The groups attribute is a dictionary mapping keys to lists of row indexes
    print grouped_data.groups
    
# Group by multiple columns
if False:
    grouped_data = example_df.groupby(['even', 'above_three']).sum()
    print grouped_data
    
# Get sum of each group
if False:
    grouped_data = example_df.groupby('even')
    print grouped_data.sum()
    
# Limit columns in result
if True:
    grouped_data = example_df.groupby('even')
    
    # You can take one or more columns from the result DataFrame
    print grouped_data.sum()['value']
    
    print '\n' # Blank line to separate results
    
    # You can also take a subset of columns from the grouped data before 
    # collapsing to a DataFrame. In this case, the result is the same.
    


# In[10]:

filename = 'nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

### Write code here to group the subway data by a variable of your choice, then
### either print out the mean ridership within each group or create a plot.


# In[20]:

a = subway_df.groupby('hour').sum()[['ENTRIESn_hourly', 'EXITSn_hourly']]


# In[41]:

#a['ENTRIESn_hourly'].astype(int)
a.index.astype(str)


# In[42]:




ind = a.index  # the x locations for the groups
width = 2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, a['ENTRIESn_hourly'].astype(int), width, color='r')


rects2 = ax.bar(ind + width, a['EXITSn_hourly'].astype(int), width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('Entries/Exits in ')
ax.set_xlabel('Hour')
ax.set_title('Entries and Exits hourly')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(ind.astype(str))

plt.show()


# In[36]:



