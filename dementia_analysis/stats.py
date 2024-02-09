"""
Implement functions to easily handle group comparisons and analyze 
relationships between variables.
"""

import statsmodels.api as sm
from scipy.stats import stats
from statsmodels.formula.api import ols


def perform_ttest(col1, col2):
    """
    Conducts a T-test for comparing the means of two groups.
    Args: col1 - numeric column/Series, col2 - numeric column/Series
    Returns: tuple with test-statistic and p-value
    """
    return stats.ttest_ind(col1, col2)


def perform_anova(df, col, group):
    """
    Performs ANOVA to compare means across multiple groups.
    Args: a number of numeric columns/Series
    Returns: tuple with F-statistic and p-value
    """
    # Ordinary Least Squares (OLS) model
    model = ols(f"{col} ~ C({group})", data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table


def calculate_correlation(df, col1, col2):
    """
    Calculates correlation coefficients between two continuous variables.
    Args: a data frame, col1 - numeric column/Series, col2 - numeric column/Series
    Returns: the correlation coefficient estimate
    """
    corr, _ = stats.pearsonr(df[col1], df[col2])
    return corr


def perform_regression(df, y, *args):
    """
    Conducts a linear regression analysis to explore relationships between variables.
    Args: a data frame, y_label - a column/series, and feature variables, seperated by a comma
    Returns: a summary table
    """
    col_list = []
    for name in args:
        col_list.append(name)
    x = df[col_list]
    model = sm.OLS(y, x).fit()
    return model.summary()
