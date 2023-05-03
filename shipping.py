weight = 41.5
cost_ground_premium = 125.00

#Ground Shipping
if weight < 2:  
  cost_ground = (weight * 1.5) + 20.0
elif weight < 2 or weight <= 6:
  cost_ground = (weight * 3.0) + 20.0
elif weight < 6 or weight <= 10:
  cost_ground = (weight * 4.0) + 20.0
else:
  cost_ground = (weight * 4.75) + 20.0

#Drone Shipping
if weight < 2:  
  cost_drone = (weight * 4.5)
elif weight < 2 or weight <= 6:
  cost_drone = (weight * 9.0)
elif weight < 6 or weight <= 10:
  cost_drone = (weight * 12.0)
else:
  cost_drone = (weight * 14.25)

print("Original weight: " + str(weight))
print("Ground shipping price: $" + str(cost_ground))
print("Ground premium shpping price: $" + str(cost_ground_premium))
print("Drone shipping price: $" + str(cost_drone))