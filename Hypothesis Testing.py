import pandas as pd
from scipy import stats

# 1. Dataset Load Karein
df = pd.read_excel('ApexPlanet_DataAnalytics_Dataset_2.xlsx')

# 2. Data ko Male aur Female me alag karein
male_sales = df[df['Gender'] == 'Male']['Total_Sales']
female_sales = df[df['Gender'] == 'Female']['Total_Sales']

# 3. T-Test perform karein
t_stat, p_value = stats.ttest_ind(male_sales, female_sales, equal_var=False)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# 4. Result Interpret Karein
if p_value < 0.05:
    print("Conclusion: We reject the Null Hypothesis. There is a significant difference in spending between genders.")
else:
    print("Conclusion: We fail to reject the Null Hypothesis. Gender does not significantly affect spending.")