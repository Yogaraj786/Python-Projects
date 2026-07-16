import numpy as np

product_ids = np.array([101,102,103,104,105,106,107,108])

prices = np.array([500, 1200, 800, np.nan, 1500, 700, np.nan, 2000])

quantity = np.array([2, 1, 3, 2, 1, 4, 2, 1])

#Replace NaN in prices with mean price
NanMean=np.nanmean(prices)

print("Nan mean Values :",NanMean)


Cleaned_price=np.where(np.isnan(prices),NanMean,prices)

print("Cleaned Price :",Cleaned_price)

#Calculate Total Revenue per 

Total_revenue=Cleaned_price*quantity

print("Total Revenue of the Products :",Total_revenue)


#Apply Discount:
#Discount amount

Discount_amount=np.where(Cleaned_price>1500,Cleaned_price*0.20,
                         np.where(Cleaned_price>1000,Cleaned_price*0.10,0))

print("Discount Amount Is :",Discount_amount)

#Final price after discount
Final_price=Cleaned_price-Discount_amount
print("The Final Price After The Discount :",Final_price)

#Total Revenue After Discount

Discount_After_revenue=Final_price*quantity
print("Total Revenue After The Discount Is :",Discount_After_revenue)

#Find Top Selling Product --👉 Based on:---Highest revenue:
top_index = np.argmax(Discount_After_revenue)
top_product_id = product_ids[top_index]

print("Highest Revenue of the product :",top_product_id)


#Statistics---Total revenue---Average revenue---Max revenue product

Total_Revenue_Amount=np.sum(Discount_After_revenue)

Average_Revenue=np.average(Discount_After_revenue)

Maximum_Revenue=np.max(Discount_After_revenue)

print("Total Revenue Amount :",Total_Revenue_Amount)
print("Average Revenue Amount :",Average_Revenue)
print("Maximum Revenue of the product :",Maximum_Revenue)



#Filtering----Products with revenue > 2000---Products with price < 800

high_revenue_products = product_ids[Discount_After_revenue > 2000]
print(high_revenue_products)


low_price_products = product_ids[Cleaned_price < 800]
print("Low Price Products:", low_price_products)


#Count of high-value products (>1500)
high_value_products = product_ids[Cleaned_price > 1500]
count_high_values_product = len(high_value_products)

print("Count Of High Value product :",count_high_values_product)


#Percentage of Discounted Products:

discounted_count = np.sum(Discount_amount > 0)
total_products = len(product_ids)
discount_percentage = (discounted_count / total_products) * 100

print("Percentage of Discounted Products :",discount_percentage)








