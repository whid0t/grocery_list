# Made by whid0t on 8th September 2020.ab

print("Hi and welcome to my console app for checking total cost of your grocery shopping.")

shopping_list = []


# Adding items to your list:
def add_items():
  count = input("Enter count of your items(min - 1, max - 5): ")
  for x in range(0, int(count)):
    item = input("Enter items you want to add: ")
    shopping_list.append(item)
  
  

# Dics for stock and prices:
stock = {
  'banana': 6,
  'apple': 0,
  'orange': 32,
  'pear': 15
}
    
prices = {
  'banana': 4,
  'apple': 2,
  'orange': 1.5,
  'pear': 3
}


#Checking the total cost:
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  print(total)

add_items()
compute_bill(shopping_list)

