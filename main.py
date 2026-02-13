import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

#1. Dataset Description

#https://www.kaggle.com/datasets/rajatsurana979/fast-food-sales-report/data
file = 'data.csv'
df = pd.read_csv(file)

#Observe data
#print(df.head())

#2. Data Cleaning and Preprocessing

#Check for Missing Values
#print(df.isnull().sum())

#Fill missing values in 'transaction_type' with 'Credit Card'
df['transaction_type'] = df['transaction_type'].fillna('Credit Card')

#Fix date time
df['date'] = pd.to_datetime(df['date'], dayfirst=False, format='mixed')

#Check Again
print(df.isnull().sum())

#3. Exploratory Data Analysis (EDA)
 
#Time Preference
# items = df['item_name'].unique()
# print(items)
time_order = ['Morning', 'Afternoon', 'Evening', 'Night', 'Midnight']

g = sns.FacetGrid(df, col="item_name", col_wrap=3, height=4, sharex=False)
g.map(sns.countplot, "time_of_sale", order=time_order)

# Clean up titles
g.set_titles("{col_name}") 
g.set_axis_labels("", "Quantity Sold")

#Monthly Sales
df['Month_Year'] = df['date'].dt.to_period('M')

monthly_sales = df.groupby('Month_Year')['transaction_amount'].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', color='blue', linewidth=2.5, markersize=8)

plt.title('Monthly Revenue Trend', fontsize=14)
plt.ylabel('Total Sales in Baht')
plt.xlabel('Month')
plt.ylim(bottom=15000)
plt.ylim(top=30000)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)

#4. Descriptive Statistics

columns = ['transaction_amount', 'quantity', 'item_price']
desc_stats = df[columns].describe()
desc_stats.loc['median'] = df[columns].median()
desc_stats.loc['IQR'] = desc_stats.loc['75%'] - desc_stats.loc['25%']
print(desc_stats.round(2))

#5. Basic Statistical Inference

data = df['transaction_amount']
mean_val = np.mean(data)
sem = stats.sem(data) # Standard Error (Variation)
ci = stats.t.interval(0.95, len(data)-1, loc=mean_val, scale=sem)

plt.figure(figsize=(8, 6))

sns.barplot(x='received_by', y='transaction_amount', data=df, 
            errorbar=('ci', 95), capsize=0.1, palette='pastel')

plt.title('Inference: Spending by Gender (with 95% CI)', fontsize=14)
plt.ylabel('Average Transaction Amount (Baht)')
plt.xlabel('Gender')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()