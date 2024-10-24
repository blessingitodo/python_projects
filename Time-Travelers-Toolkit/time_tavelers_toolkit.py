import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

current_date = dt.date.today()
current_time = dt.datetime.now().time()
print(current_date)
print(current_time)

def random_year(start, end):
  year = randint(start, end)
  return year
target_year = random_year(1900, 2100)
def base_cost(price):
  cost = Decimal(f'{price}')
  return cost

time_traveled = abs(current_date.year - target_year)

final_cost = round((base_cost(1000.00) * time_traveled), 2)

destinations_list = ["Kyoto", "Cape Town", "Santorini", "Machu Picchu", "Reykjavik", "Rome", "Queenstown", "Bali", "Dubai", "Banff"]

destination = choice(destinations_list)

print(custom_module.generate_time_travel_message(target_year, destination, final_cost))