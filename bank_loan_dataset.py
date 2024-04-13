# -*- coding: utf-8 -*-
"""Bank_Loan_Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14r2fCoGRznAeRFPVQeK8912e3f2xEaUO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



from google.colab import files
uploaded = files.upload()

df = pd.read_csv('/content/sample_data/samplebankloandata.xlsx - Sheet1.csv')
print(df.head())
print(df.tail())

print(df.dtypes)

print(df.isnull().sum())

df.describe()

sns.histplot(data=df,x="loan_amount",kde=True)
plt.title("Distribution of the loan amount")
plt.xticks(rotation=45)
plt.show()

sns.countplot(data=df,x="purpose")
plt.xticks(rotation=45)
plt.title('Loan Count By purpose')
plt.show()

sns.barplot(data=df,x='purpose',y='loan_amount',estimator=np.mean)
plt.xticks(rotation=90)
plt.title('Average Loan By Purpose')
plt.show()

plt.pie(df['region'].value_counts(),labels=df['region'].value_counts().index,autopct='%1.1f%%')
plt.title('Region wise Loan Distribution')
plt.show()

df1 = df[['annual_inc','loan_amount','interest_rate','total_pymnt']]
corr= df1.corr()
sns.heatmap(corr,annot=True,cmap='viridis')
plt.title('Correlation Heatmap')
plt.show()

sns.boxplot(data=df,x='grade',y='dti',showfliers=False)
plt.title('Loan Quality based on dti ratio')
plt.show()

df['Year-term']=df['year'].astype(str) +'-'+ df['term'].astype(str)
df.groupby('Year-term')['total_pymnt'].sum().plot()
plt.title('Monthly Loan Over Time')
plt.xticks(rotation=45)
plt.show()

df['Year-grade']=df['year'].astype(str) +'-'+ df['grade'].astype(str)
df.groupby('Year-grade')['total_pymnt'].sum().plot()
plt.title('Monthly Loan Over Time by Grade')
plt.xticks(rotation=45)
plt.show()

sns.scatterplot(data=df, x='purpose', y='interest_rate')
plt.title('Purpose VS Interest rate')
plt.show()

import plotly.express as px

fig = px.scatter_3d(df, x='loan_amount', y='term', z='interest_rate',
                  color='purpose')
fig.update_layout(scene = dict(
                    xaxis = dict(title  = 'Loan Amount'),
                    yaxis = dict(title  = 'Term'),
                    zaxis = dict(title  = 'Interest Rate')))
fig.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['loan_amount'], df['interest_rate'], df['grade_cat'])
ax.set_xlabel('Loan Amount')
ax.set_ylabel('Interest Rate')
ax.set_zlabel('Grade')
plt.title("3D Chart of Loan amount, Interest rate and Grade")
plt.show()