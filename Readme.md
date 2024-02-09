# MAC AI Office Hours 
## Analysis of Simulated Data on Dementia 
---

### Introduction

The data on dementia represents a simulated data set with 1000 rows and 21 columns. The primary outcome of interest is the "Clinical Dementia Rating Total Score" measured as a numeric variable 

### Collaborators
Alfa Yansane

### Installations
```
import dementia_analysis
```

### Function Use

##### import module
---
1. load_data: Import CSV files into a pandas DataFrame.Takes file path input and returns pandas DataFrame containing the dataset.
```
load_data("this/is/my/file.csv")
``` 

##### viz module
2. plot_distribution: Plots the distribution of a specified column. Takes in a data frame, a specified column, a title, and returns a plot (either a histogram for continuous data or a barplot for categorical data)
```
plot_distribution(dataframe, column_in_dataframe, title)
```

3. plot_boxplot: Creates boxplots to visualize group differences based on a specified categorical variable. Takes in a data frame, a specified column, a categorical variable, and returns a boxplot.
```
plot_boxplot(dataframe, column_in_dataframe, categorical_var)
```

4. plot_correlation_matrix: Generates a correlation matrix plot to visualize correlations between continuous variables. Takes in a data frame and provides all pairwise correlations between continously measured variables in the dataframe.
```
plot_correlation_matrix(dataframe)
```

5. scatter_plot: Plots a scatter plot to visualize the relationship between two continuous variables.Takes in 2 numeric columns from a data frame and returns the scatter plot.
```
scatter_plot(datarame, col1_from_df, col2_from_df)
```

##### stats module
6. perform_ttest: Conducts a T-test for comparing the means of two groups. Takes in two numeric columns of the same length and returns the t-statistic and a p-value
```
perform_ttest(column_1, column_2)
```

7. perform_anova: Performs ANOVA to compare means across multiple groups. Takes in 3 or more numeric columns of the same length and returns the F-statistic and a p-value
```
perform_anova(column_1, column_2, column_3)
perform_anova(column_1, column_2, column_3, column_4)
```

8. calculate_correlation: Calculates correlation coefficients between two continuous variables. Takes in 2 numeric columns of the same length and returns the correlation coefficient
```
calculate_correlation(column_1, column_2)
```

9. perform_regression: Conducts a linear regression analysis to explore relationships between variables. Takes in a data matrix (x) which consists of feature variables and a column (y) vector/Series representing the label/outcome variable.
```
perform_regression(x, y)
```







