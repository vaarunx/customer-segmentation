# customer-segmentation

Any business is heavily reliant on its customers and its important to keep them happy and satisfied. So it is as equally important to also know what are their needs, how much are their needs and when do they need. 

In business it is also important to know your target audience clearly to have a perfect understanding of the supply design your business needs. By knowing the target audience, it helps us determine where to focus more to sell the product and also helps increase sales as we, now are selling the product to a whole buying group instead of individual customers.

The above two can be done by using Data mining clustering algorithms on the customer database to identify the target audience and increase sales in the business.


### Atrributes ###

| Attributes          | Description                                                        |
|---------------------|--------------------------------------------------------------------|
| ID                  | Customer’s Unique Identifier                                       |
| Year_Birth          | Year of Birth of the Customer                                      |
| Education           | Customer’s Education Level                                         |
| Marital_Status      | Customer’s Marital Status                                          |
| Income              | Customer’s yearly household income                                 |
| Kidhome             | Number of children                                                 |
| Teenhome            | Number of teens                                                    |
| Dt_Customer         | Date of customer’s enrollment with the company                     |
| Recency             | Number of days since customer’s last purchase                      |
| Complain            | 1 if the customer complained in the last 2 years, 0 otherwise      |
| MntWines            | Amount spent on wine in the last 2 years.                          |
| MntFruits           | Amount spent on fruits in the last 2 years.                        |
| MntMeatProducts     | Amount spent on meat in the last 2 years.                          |
| MntFishProducts     | Amount spent on fish in the last 2 years                           |
| MntSweetProducts    | Amount spent on sweets in the last 2 years                         |
| MntGoldProds        | Amount spent on gold in the last 2 years                           |
| NumDealsPurchases   | Number of purchases made with a discount                           |
| AcceptedCmp1        | 1 if customer accepted the offer in the 1st campaign, 0 otherwise  |
| AcceptedCmp2        | 1 if customer accepted the offer in the 2nd campaign, 0 otherwise  |
| AcceptedCmp3        | 1 if customer accepted the offer in the 3rd campaign, 0 otherwise  |
| AcceptedCmp4        | 1 if customer accepted the offer in the 4th campaign, 0 otherwise  |
| AcceptedCmp5        | 1 if customer accepted the offer in the 5th campaign, 0 otherwise  |
| Response            | 1 if customer accepted the offer in the last campaign, 0 otherwise |
| NumWebPurchases     | Number of purchases made through the company’s website             |
| NumCatalogPurchases | Number of purchases made using a catalogue                         |
| NumStorePurchases   | Number of purchases made directly in stores                        |
| NumWebVisitsMonth   | Number of visits to company’s website in the last month            |

### Results ###

The different clusters are named as,
  * Upper Class
  * Upper Middle Class
  * Lower Middle Class 
  * Lower Class

1. Division of Clusters

<img width="672" alt="Screenshot 2022-01-10 at 1 44 33 AM" src="https://user-images.githubusercontent.com/50340089/148699118-3bf6e01f-9a78-46a1-9281-f56fbbb94ab0.png">


2. Total Spending by Clusters

<img width="682" alt="Screenshot 2022-01-10 at 1 45 43 AM" src="https://user-images.githubusercontent.com/50340089/148699159-b72f66d9-a9d4-463f-b5d3-fc093d9c215b.png">

* It is very obvious that the upper class contribute to more than half of the total sales followed by the upper middle class by 35% and then by lower middle class and then finally followed by the lower class with a measly 2.4%


3. Cluster-wise spendings

<img width="1133" alt="Screenshot 2022-01-10 at 1 46 08 AM" src="https://user-images.githubusercontent.com/50340089/148699201-96f9f1cf-88fb-434a-bbab-e75a1493eff3.png">

* All the classes are found to spend the most on wines and then followed by meat products.


4. Purchasing Manner of the clusters
<img width="1132" alt="Screenshot 2022-01-10 at 1 46 17 AM" src="https://user-images.githubusercontent.com/50340089/148699210-895a9a36-e673-466d-8c98-522b08490535.png">

* The lower class visits the website a lot but doesn't buy products from web often. 
* The top 2 classes are purchasing a considerable amount from the online store compared to the other 2 classes.
* The number of purchases made from deals are also suprisingly low for both the lower class and the upper class. 


5. Which Marketing Campaign favoured which type of clusters?

<img width="1129" alt="Screenshot 2022-01-10 at 1 46 24 AM" src="https://user-images.githubusercontent.com/50340089/148699227-2a08a312-3c2f-4b2f-b9d8-b5b0e1adb9c0.png">

* The first and the fifth campaign had a very positive result from the upper class but had very poor results from other classes.
* The second campaign had extremely poor results overall.
* The third and the fourth campaign had decent results from nearly all the classes.

### Conclusion ###

It is seen that the store, web-store and the campaigns are mainly catered to the upper classes of the society and the lower and the lower middle class do not buy that many products compared to the other 2 classes. Even the campaigns fail to spark a boost in the lower sections of the society. The store should provide a better campaign that focuses on the lower and the lower middle class to improve their numbers.






