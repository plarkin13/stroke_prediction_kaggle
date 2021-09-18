import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Convert a single string from snake_case to normal written language (with capitalization options!):

# Let's make the default behavior capitalizing the first letter of the input string
def convert_snake_case(label, capitalize_first=True, capitalize_all=False):
    """Takes an input string assumed to be in snake case and returns it with spaces inserted and capitalized to your liking.

    Keyword Arguments:
    label: a_snake_case_string
    capitalize_first: Bool, capitalize the first word of the string
    capitalize_all: Bool, capitalize all words of the string"""

    if capitalize_all:
        return ' '.join([word.capitalize() for word in label.split('_')])
    elif capitalize_first:
        return ' '.join([word.capitalize() if i == 0 else word for i, word in enumerate(label.split('_'))])
    else:
        return ' '.join([word for word in label.split('_')])


# Convert a single string from CamelCase to normal written language:

# By default, we will coerce all uppercase letters in the string to lowercase
def convert_camel_case(label, capitalize_first=True, capitalize_all=False):
    """Takes an input string assumed to be in camel case and returns it with spaces inserted and capitalized to your liking.

    Keyword Arguments:
    label: CamelCaseString
    capitalize_first: Bool, capitalize the first word of the output string
    capitalize_all: Bool, capitalize all words of the output string
    
    Adapted from https://stackoverflow.com/a/44969381"""
    
    
    if capitalize_all:
        return ''.join([' '+c if c.isupper() else c for c in label]).lstrip(' ')
    elif capitalize_first:
        return ''.join([' '+c if c.isupper() and i == 0 else ' '+c.lower() if c.isupper() else c.lower() for i, c in enumerate(label)]).lstrip(' ')
    else:
        return ''.join([' '+c.lower() if c.isupper() else c for c in label]).lstrip(' ')



def my_hist(data, x_col, title, x_label, y_label='Frequency', size_var = 18):
    # set size_var as a parameter with a default of 18
    plt.figure(figsize=(6,10));


    # abstract the dataframe as parameter, data
    # abstract the column string for the "x" axis as a parameter, x_col
    sns.displot(x = data[x_col]);
    
    # abstract title as parameter
    plt.title(title, fontsize = size_var, pad = size_var / 2);
    
     # abstract the "x" axis lavel as a parameter, x_label
    plt.xlabel(x_label, fontsize = size_var, labelpad = size_var/2)
    plt.xticks(fontsize=size_var/2, rotation=45)
    
    plt.ylabel(y_label, fontsize = size_var, labelpad = size_var/2)
    plt.yticks(fontsize=size_var/2, rotation=90);



def my_barplot(data, x_col, y_col, title, x_label, y_label, size_var = 18):
    # set size_var as a parameter with a default of 18
    plt.figure(figsize=(10,6))
    # abstract title as parameter
    plt.title(title, fontsize = size_var, pad = size_var / 2)

    # abstract the dataframe as parameter, data
    # abstract the column string for the "x" axis as a parameter, x_col
    # abstract the column string for the "y" axis as a parameter, y_col
    sns.barplot(x = data[x_col], y = data[y_col]);

    # abstract the "x" axis lavel as a parameter, x_label
    plt.xlabel(x_label, fontsize = size_var, labelpad = size_var/2)
    plt.xticks(fontsize=size_var/2, rotation=45)

    # abstract the "y" axis lavel as a parameter, y_label
    plt.ylabel(y_label, fontsize = size_var, labelpad = size_var/2)
    plt.yticks(fontsize=size_var/2, rotation=90);



def my_scatterplot(data, x_col, y_col, title, x_label, y_label, alpha=.1, size_var = 18):
    # set size_var as a parameter with a default of 18
    plt.figure(figsize=(10,6))
    # abstract title as parameter
    plt.title(title, fontsize = size_var, pad = size_var / 2)

    # abstract the dataframe as parameter, data
    # abstract the column string for the "x" axis as a parameter, x_col
    # abstract the column string for the "y" axis as a parameter, y_col
    sns.scatterplot(x = data[x_col], y = data[y_col], alpha=alpha);

    # abstract the "x" axis lavel as a parameter, x_label
    plt.xlabel(x_label, fontsize = size_var, labelpad = size_var/2)
    plt.xticks(fontsize=size_var/2, rotation=45)

    # abstract the "y" axis lavel as a parameter, y_label
    plt.ylabel(y_label, fontsize = size_var, labelpad = size_var/2)
    plt.yticks(fontsize=size_var/2, rotation=90);



def all_corr_heatmap(data, title, size_var = 18, incl_annot = True):
    # set size_var as a parameter with a default of 18
    plt.figure(figsize=(10,6))
    # abstract title as parameter
    plt.title(title, fontsize = size_var, pad = size_var / 2)
    
    sns.heatmap(data.corr(), cmap='coolwarm', vmin = -1, vmax = 1, annot = incl_annot)
    
    
    

def one_corr_heatmap(data, target_variable, title, x_label, size_var = 18, use_abs = False):
    # set size_var as a parameter with a default of 18
    plt.figure(figsize=(4,10))
    # abstract title as parameter
    plt.title(title, fontsize = size_var, pad = size_var / 2)
    
    sns.heatmap(data.corr()[[target_variable]].sort_values(by=target_variable, 
                                                           ascending = False, 
                                                           key = np.abs if use_abs else None)[1:], 
                cmap='coolwarm', vmin = -1, vmax = 1, annot = True)
    
    # abstract the "x" axis lavel as a parameter, x_label
    plt.xlabel(x_label, fontsize = size_var, labelpad = size_var/2)
    plt.xticks(fontsize=size_var/2)

    # abstract the "y" axis lavel as a parameter, y_label
    plt.yticks(fontsize=size_var/2);
    
    
