# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:24:07 2023

@author: TAMILSELVAN
"""

# Imported libraries:
import pandas as pd  # Inputing file (eg, pd.read_csv), Data-processing
import numpy as np  # Linear Algebra
import matplotlib.pyplot as plt  # Visualisation
import seaborn as sns  # Visualisation
import warnings  # Supress warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('food_prod_data.csv', index_col=0)  # Reading the file as df
print(df)

# Function:1(defining the line plot for visualisation)

def linePlot(linePlotData):
    '''Defining the function to create the lineplot,then applyig the dataframe
into the function, labelling the X-axis and Y-axis, Naming the lineplot,
Create legend in upper right corner'''

    sns.set_style("whitegrid")  # Use seaborn style
    linePlotData.plot(x='Years', y=['Afghanistan', 'Bangladesh', 'Bhutan',
                                    'India', 'Maldives', 'Nepal',
                                    'Pakistan', 'Sri Lanka'],
                      kind='line', figsize=(16, 6), marker='o')
    plt.title('Food Production Index of Southern Asia')
    plt.xlabel('Years')
    plt.ylabel('Production Index rate')
    plt.legend(loc='upper right')


# Function:2(defining the bar plot for visualisation)

def barPlot(barData):
    '''Defining the function to create the barplot to compare the two
countries, then applyig the dataframe into the function, labelling the X-axis
and Y-axis, Naming the barplot, Create legend in upper right corner'''

    sns.set_style("whitegrid")
    barData.plot(x='Years', y=['India', 'Maldives'], kind='bar',
                 color=('blue', 'green'), width=0.65)
    plt.title('Comparison of India and Maldives Food Production')
    plt.figure(figsize=(16, 6))
    plt.xlabel('Years')
    plt.ylabel('Production rate')
    plt.legend(loc='upper right')
    plt.show()


# Function:3(defining the scatter plot for visualisation)

def scatterPlot(data, x_feature, y_feature, title, x_label, y_label, position):
    '''Defining the funtion to create the subplot of scatterplot of all 
selected countries, then applying dataframe into the function, labelling 
the X-axis and Y-axis, Naming all scatterplot and creating legends'''

    sns.set_style("whitegrid")  # Use seaborn style
    ax = plt.subplot(2, 4, position)
    data.plot(x=x_feature, y=y_feature, kind='scatter', ax=ax, marker='o',
              figsize=(16, 8))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()  #Making space between each scatter plot
    plt.show()

# Function:4(defining the pie plot for visualisation)

def piePlot(data, Years, fontsize=11):
    '''Using pieplot to compare the percentage of all seleted Countries Food 
production index of year 2001 and 2021, so taking the dataframe of df1, 
which is the dataframe of before transposing '''

    label = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 
             'Nepal', 'Pakistan', 'Sri Lanka']
    plt.figure(figsize=(4, 5))
    plt.pie(data[str(Years)], autopct='%1.0f%%', labels=label, startangle=90)
    plt.title(f'Food Production Index in {Years}', fontsize=fontsize)
    plt.show()


# Main program
# Selecting the valuable rows because last 5 rows are nugatory:
df = df.iloc[:-5]
# Changing the '..' into 'NaN' value:
df.replace('..', np.nan, inplace=True)
# Renaming the column into relevant way:
df = df.rename(columns={'2001 [YR2001]': '2001', '2002 [YR2002]': '2002',
                        '2003 [YR2003]': '2003', '2004 [YR2004]': '2004',
                        '2005 [YR2005]': '2005', '2006 [YR2006]': '2006',
                        '2007 [YR2007]': '2007', '2008 [YR2008]': '2008',
                        '2009 [YR2009]': '2009', '2010 [YR2010]': '2010',
                        '2011 [YR2011]': '2011', '2012 [YR2012]': '2012',
                        '2013 [YR2013]': '2013', '2014 [YR2014]': '2014',
                        '2015 [YR2015]': '2015', '2016 [YR2016]': '2016',
                        '2017 [YR2017]': '2017', '2018 [YR2018]': '2018',
                        '2019 [YR2019]': '2019', '2020 [YR2020]': '2020',
                        '2021 [YR2021]': '2021', '2022 [YR2022]': '2022'})
# Checking is any null value presented in data:
print(df.isnull().sum())
# Droping the unwanted columns from the dataset:
df1 = df.drop(['Country Code', 'Series Name', 'Series Code', '2022'], axis=1)
# Transpoing the dataframe to access the country as column variable:
df1_trans = df1.transpose()
# Getting information of the dataframe:
print(df1_trans.info())
# Checking for the duplicated values:
print(df1_trans.duplicated().value_counts())
# Changing the first column as index column:
df2 = df1_trans.reset_index(drop=True)
# Adding a column of 'Years' to the dataframe:
year = pd.Series([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
                  2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
                  2021],
                 dtype=object)
df2['Years'] = year
# df_final is a new DataFrame, the last column 'year is moved to the first one
df_final = pd.concat([df2.iloc[:, -1:], df2.iloc[:, :-1]], axis=1)

# Visualisation-1(lineplot)
linePlot(df_final)
# Visualisation-2(barplot)
barPlot(df_final)
# Visualisation-3(subplot of scatterplot)
scatterPlot(df_final, 'Years', 'Afghanistan',
            'Afghanistan', 'years', 'production index', 1)
scatterPlot(df_final, 'Years', 'Bangladesh',
            'Bangladesh', 'years', 'production index', 2)
scatterPlot(df_final, 'Years', 'Bhutan', 'Bhutan',
            'years', 'production index', 3)
scatterPlot(df_final, 'Years', 'India', 'India',
            'years', 'production index', 4)
scatterPlot(df_final, 'Years', 'Maldives', 'Maldives',
            'years', 'production index', 5)
scatterPlot(df_final, 'Years', 'Nepal', 'Nepal',
            'years', 'production index', 6)
scatterPlot(df_final, 'Years', 'Pakistan', 'Pakistan',
            'years', 'production index', 7)
scatterPlot(df_final, 'Years', 'Sri Lanka',
            'Sri Lanka', 'years', 'production index', 8)
# Visualisation-4(pieplot)
piePlot(df1, 2001)
piePlot(df1, 2021)
