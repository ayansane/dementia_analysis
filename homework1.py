# %%
from dementia_analysis.importer import load_data
from dementia_analysis.stats import (
    calculate_correlation,
    perform_anova,
    perform_regression,
    perform_ttest,
)
from dementia_analysis.viz import (
    plot_boxplot,
    plot_correlation_matrix,
    plot_distribution,
    scatter_plot,
)

# %
# %%
file_path = "/https://github.com/pinheirochagas/mac_ai/blob/da2c6e3293668e76e01954d215746b2674c3673b/homework/hw1/simulated_cognitive_tests_dataset.csv"
df = load_data(file_path)
df.head()
# %%
plot_distribution(df, "Age")
# %%
plot_boxplot(df, "Clinical Dementia Rating Total Score", "Gender")
# %%
plot_correlation_matrix(df["Age"], df["Clinical Dementia Rating Total Score"])
# %%
scatter_plot(df, "Trail Making Test", "Digit Task")
# %%
female = df[df["Gender"] == "Female"]
male = df[df["Gender"] == "Male"]

result_ttest = perform_ttest(female["Age"], male["Age"])
print(result_ttest)
# %%
result_correlation = calculate_correlation(df, "Global Cognition", "Trail Making Test")
print(result_correlation)
# %%
result_anova = perform_anova(df, "Age", "Diagnosis")
print(result_anova)
# %%
y = df["Clinical Dementia Rating Total Score"]
result_regression = perform_regression(
    df, y, "Age", "Digit Backward"
)
print(result_regression)
# %%
