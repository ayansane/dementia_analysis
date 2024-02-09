"""
    Develop function to plot data distribution and visualize group differences
    and correlations
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 


def plot_distribution(df, col, title):
    """
    Plots the distribution of a specified column (e.g., age, test scores)
    Args: col1 - numeric column/Series, col2 - numeric column/Series
    Returns: tuple with test-statistic and p-value
    """
    if df[col].dtype == "object":
        df[col].value_counts().sort_values().plot(kind="bar")
    else:
        ax = sns.histplot(df[col])
        ax.set_title(title)


def plot_boxplot(df, col, group):
    """
    Creates boxplots to visualize group differences based on a
    specified categorical variable (e.g., gender, diagnosis)

    Args: df - pandas data frame, col1 - numeric column/Series, group - categorical var
    Returns: tuple with test-statistic and p-value
    """
    ax = sns.boxplot(data=df, x=col, y=group)
    ax.set_title(f"Boxplot of {col} by {group}")


def plot_correlation_matrix(x, y):
    """
    Generates a correlation matrix plot to visualize correlations
    between continuous variables.

    Args: df - pandas data frame
    Returns: a correlation matrix
    """
    r = np.corrcoef(x, y)
    plt.matshow(r)


def scatter_plot(df, col1, col2):
    """
    Conducts a T-test for comparing the means of two groups.
    Args: df - pandas data frame, col1 - numeric column/Series, col2 - numeric column/Series
    Returns: scatter plot
    """
    ax = sns.scatterplot(data=df, x=col1, y=col2)
    ax.set_xlabel(col1)
    ax.set_ylabel(col2)
    ax.set_title(f"Scatter Plot of {col1} by {col2}")
    # plt.scatter(df[col1], df[col2])
    # plt.title(f"Scatter Plot of {col1} by {col2}")
    # plt.xlabel(col1)
    # plt.ylabel(col2)


plt.show()
