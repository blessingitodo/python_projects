weight = 41.5
flat_charge = 20

#Ground Shipping
if weight <= 2:
  cost = flat_charge + weight*1.50
elif weight > 2 and weight <= 6:
  cost = flat_charge + weight*3.00
elif weight > 6 and weight <= 10:
  cost = flat_charge + weight*4.00
elif weight > 10:
  cost = flat_charge + weight*4.75
print("Cost of Ground Shipping: $", cost)

#Ground Shipping Premium
premium_cost = 125
print("Cost of Premium Ground Shipping: $", premium_cost)

#Drone Shipping
drone_flatcharge = 0
if weight <= 2:
  cost = drone_flatcharge + weight*4.50
elif weight > 2 and weight <= 6:
  cost = drone_flatcharge + weight*9.00
elif weight > 6 and weight <= 10:
  cost = drone_flatcharge + weight*12.00
elif weight > 10:
  cost = drone_flatcharge + weight*14.25
print("Cost of Drone Shipping is: $", cost)