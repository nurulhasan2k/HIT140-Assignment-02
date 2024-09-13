import matplotlib.pyplot as plt
import pandas as pd

#Nurul Hasan's part starts

#import datasets
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')

##data wrangling
#merge datasets
merged_data = dataset1.merge(dataset2, on='ID').merge(dataset3, on='ID')

#check for missing values
print(merged_data.isnull().sum())

#handle missing
merged_data.fillna(merged_data.mean(), inplace=True)

#screentime analysis
screen_time_cols = ['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']
print(merged_data[screen_time_cols].describe())

#histogram
merged_data[['C_we', 'C_wk']].hist()
plt.title('Computer Usage: Weekends vs Weekdays')
plt.show()

#Nurul Hasan's part starts

#Praggawn's part starts
print(merged_data['gender'].value_counts())
print(merged_data['minority'].value_counts())

merged_data['gender'].value_counts().plot(kind='bar')
plt.title('Gender Distribution')
plt.show()
#Praggawn's part ends

#Bidur's part start#
from scipy.stats import ttest_ind, pearsonr

group_male = merged_data[merged_data['gender'] == 1]['Optm']
group_female = merged_data[merged_data['gender'] == 0]['Optm']
t_stat, p_value = ttest_ind(group_male, group_female)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
#Bidur's part end#

#Raianul's part start#
corr, p_val = pearsonr(merged_data['S_we'], merged_data['Relx'])
print(f"Correlation: {corr}, P-value: {p_val}")
#Raianul's part end#
