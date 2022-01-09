import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans

import datetime as dt

df = pd.read_csv("/content/drive/MyDrive/marketing_campaign_final.csv" , sep = '\t')

df.isnull().sum()

df = df.dropna()    

df['Total_kids']= df['Kidhome'] + df['Teenhome']

df['Spending'] = df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds'] 

df['Age'] = 2021 - df.Year_Birth

df.Marital_Status = df.Marital_Status.replace({'Together': 'Married',
                                                'Divorced': 'Single',
                                                'Widow': 'Single', 
                                                'Alone': 'Single',
                                                'Absurd': 'Single',
                                                'YOLO': 'Single'}) 


df = df[df.Age < 100]
df = df[df.Income < 120000]

maritalstatus = df.Marital_Status.value_counts()
plt.pie(maritalstatus, 
             labels = maritalstatus.index,
             explode=(0.05,0.05),
             autopct='%1.1f%%')
plt.title('Marital Status Distribution')

plt.figure(figsize=(15,7))
sns.scatterplot(data=df, y='Spending', x='Income')
plt.title('Spending vs Income')

campaign = df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 
                                                  'AcceptedCmp5', 'Response']].sum()

campaign.plot(kind='bar', figsize=(15,10))
plt.title('Campaign Analysis')

X = df.drop(['ID', 'Year_Birth','Kidhome','Education', 'Marital_Status',
       'Teenhome', 'Dt_Customer', 'Recency', 'MntWines', 'MntFruits',
       'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
       'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
       'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1',
       'AcceptedCmp2', 'Complain', 'Z_CostContact', 'Z_Revenue', 'Response'], axis=1) 

model = KMeans(n_clusters=4, init='k-means++', random_state=42).fit(X)

preds = model.predict(X)

segmented_customers = X.copy()
segmented_customers['clusters'] = preds
df['clusters'] = preds

sns.violinplot(data=segmented_customers, y= 'Income', x= 'clusters')

sns.violinplot(data=segmented_customers, y= 'Total_kids', x= 'clusters')

sns.boxplot(data=segmented_customers, y= 'Spending', x= 'clusters')

sns.violinplot(data=segmented_customers, y= 'Age', x= 'clusters')


#Analysing the Clusters

segmented_customers.clusters = segmented_customers.clusters.replace({0 : 'Lower Class',
                                                           1 : 'Upper Class',
                                                           2 : 'Upper Middle Class',
                                                           3 : 'Lower Middle Class'})

df.clusters = df.clusters.replace({0 : 'Lower Class',
                                                           1 : 'Upper Class',
                                                           2 : 'Upper Middle Class',
                                                           3 : 'Lower Middle Class'})


cluster_count= segmented_customers['clusters'].value_counts()

plt.figure(figsize=(20,10))
plt.pie(cluster_count, labels= cluster_count.index, explode=(0.05, 0.05, 0.05, 0.05), autopct='%1.1f%%')
plt.title('Division of Clusters')

plt.figure(figsize=(10,7))
sns.scatterplot(data=segmented_customers, y='Spending', x='Income', hue='clusters')
plt.title('Spending and Income based on Clusters')
plt.xlabel('Income')
plt.ylabel('Spending')

cluster_total_spend = df.groupby('clusters')['Spending'].sum()

plt.figure(figsize=(20,10))
plt.pie(cluster_total_spend, labels= cluster_total_spend.index, explode=(0.05, 0.05, 0.05, 0.05), autopct='%1.1f%%')
plt.title('Total Spending by Cluster')

#Cluster Spending

cluster_spendings = df.groupby('clusters')[['MntWines', 'MntFruits','MntMeatProducts', 
                                                  'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum()

cluster_spendings.plot(kind='bar', stacked=True,figsize=(20,10))
plt.title('Cluster wise Spendings')

#Cluster Purchasing

cluster_purchases = df.groupby('clusters')[['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
                                                  'NumStorePurchases', 'NumWebVisitsMonth']].sum()

cluster_purchases.plot(kind='bar', figsize=(20,10))
plt.title('Cluster wise Purchasing habits')


#Cluster Campaigns

cluster_campaign = df.groupby('clusters')[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 
                                                  'AcceptedCmp5', 'Response']].sum()

cluster_campaign.plot(kind='bar', figsize=(20,10))
plt.title('Cluster wise Marketing Results')