from scipy.stats import (
    levene,
    mannwhitneyu,
    ttest_ind,
)


def levene_analysis(dataframe, alfa=0.05, center="mean"):
    print("Levene's Test")

    statistics_levene, p_value_levene = levene(
        *[dataframe[column] for column in dataframe.columns],
        center=center,
        nan_policy="omit",
    )

    print(f"{statistics_levene=:.3f}")
    if p_value_levene > alfa:
        print(f"Equal variances (p-value: {p_value_levene:.3f})")
    else:
        print(f"At least one variance is different (p-value: {p_value_levene:.3f})")


def ttest_ind_analysis(
    dataframe,
    alfa=0.05,
    equal_variances=True,
    alternative="two-sided",
):
    print("Student's t-test")
    statistics_ttest, p_value_ttest = ttest_ind(
        *[dataframe[column] for column in dataframe.columns],
        equal_var=equal_variances,
        alternative=alternative,
        nan_policy="omit",
    )

    print(f"{statistics_ttest=:.3f}")
    if p_value_ttest > alfa:
        print(f"Fails to reject the null hypothesis (p-value: {p_value_ttest:.3f})")
    else:
        print(f"Rejects the null hypothesis (p-value: {p_value_ttest:.3f})")


def mannwhitneyu_analysis(
    dataframe,
    alfa=0.05,
    alternative="two-sided",
):

    print("Mann-Whitney's Test")
    statistics_mw, p_value_mw = mannwhitneyu(
        *[dataframe[column] for column in dataframe.columns],
        nan_policy="omit",
        alternative=alternative,
    )

    print(f"{statistics_mw=:.3f}")
    if p_value_mw > alfa:
        print(f"Fails to reject the null hypothesis (p-value: {p_value_mw:.3f})")
    else:
        print(f"Rejects the null hypothesis (p-value: {p_value_mw:.3f})")


def remove_outliers(data, whisker_width=1.5):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    return data[(data >= q1 - whisker_width * iqr) & (data <= q3 + whisker_width * iqr)]