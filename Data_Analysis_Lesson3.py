
# coding: utf-8

# # March 30th, 2017
# ## data analysis - calculating correlation

# In[3]:

import pandas as pd


# In[2]:



filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

def correlation(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.
    
    correlation = average of (x in standard units) times (y in standard units)
    
    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''
    #for each i in x, y xi/std(x) * yi/std(y)
    
    return ( ((x-x.mean())/x.std(ddof=0))*((y-y.mean())/y.std(ddof=0))).mean()

entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

print correlation(entries, cum_entries)
print correlation(rain, temp)
print correlation(entries, rain)
print correlation(entries, temp)


# ## Dataframe Vectorized Operations

# In[14]:

entries_and_exits = pd.DataFrame({
    'ENTRIESn': [3144312, 3144335, 3144353, 3144424, 3144594,
                 3144808, 3144895, 3144905, 3144941, 3145094],
    'EXITSn': [1088151, 1088159, 1088177, 1088231, 1088275,
               1088317, 1088328, 1088331, 1088420, 1088753]
})

entries_and_exits - entries_and_exits.shift()


# In[23]:

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio', 
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)
    
def convert_grades(grades):
    '''
    Fill in this function to convert the given DataFrame of numerical
    grades to letter grades. Return a new DataFrame with the converted
    grade.
    
    The conversion rule is:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> D
        0-59   -> F
    '''
    def lettergrade(score):
        letters = {
            10: 'A',
            9: 'A',
            8: 'B',
            7: 'C',
            6: 'D'
        }
        #a = score < 60
        
        return 'F' if score < 60 else letters[score/10]
    
    return grades.applymap(lettergrade) 


# In[24]:

convert_grades(grades_df)


# ## DataFrame .apply()

# In[28]:

def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    '''
    #for each column, for each element, subtract from column mean and divide by column std
    def thething(series):
        return (series - series.mean())/series.std(ddof=0)
    return df.apply(thething)


# In[29]:

standardize(grades_df)


# In[48]:

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})

 
def second_largest(df):
    '''
    Fill in this function to return the second-largest value of each 
    column of the input DataFrame.
    '''
    #for each column, find argmax, drop array, then find max value
    def droplarge(s):
        return s.drop(s.argmax()).max()

    return df.apply(droplarge)


# In[49]:

second_largest(df)


# In[76]:

df


# In[85]:

print df.mean(axis='columns')
print df.std(ddof=0, axis='columns')
print df.subtract(df.mean(axis='columns'), axis='index')
print df.subtract(df.mean(axis='columns'), axis='index').divide(df.std(axis='columns'), axis='index')


# In[88]:

def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.
    
    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    '''
    return (df - df.mean())/df.std(ddof=0)

def standardize_rows(df):
    '''
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().
    
    This one is more challenging than standardizing each column!
    '''
    return df.subtract(df.mean(axis='columns'), axis='index').divide(df.std(ddof=0, axis='columns'), axis='index')


# In[89]:

standardize_rows(grades_df)

