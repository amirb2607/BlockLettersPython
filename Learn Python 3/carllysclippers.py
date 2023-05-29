hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#Creating total price variable
total_price = 0

for i in prices:
  total_price +=i
#Finding average haircut price
average_price = total_price / len(prices)
#Printing this price
print("Average Haircut Price: "+str(average_price))
#Using list comprehension to make a list called new_prices, which has each element in prices minus 5.
new_prices =  [price - 5 for price in prices]
print(new_prices)
#Creating new variable to store total revenue.
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])

print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
#Finding all cuts that are lower than 30
cuts_under_30 = [cut for cut in new_prices if cut < 30]
#Printing said cuts under 30
print(cuts_under_30)
