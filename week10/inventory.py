# --- EXERCISE 1 ---
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
# --- EXERCISE 2 ---
print(inventory[0])
print(inventory[-1])

middle_index = len(inventory) // 2
print(inventory[middle_index])
# --- EXERCISE 3 ---
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])
# --- EXERCISE 4 ---
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)
# --- EXERCISE 5 ---
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because their values cannot be changed accidentally.")
print(coords)
# --- EXERCISE 6 ---
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", best)
print("Worst:", worst)
# --- EXERCISE 7 ---
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)
print("Original prices:", prices)
print("Discounted prices:", discounted)
# --- EXERCISE 8 ---
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
count = len(high_sales)
average = sum(high_sales) / count
print(high_sales)
print("Count:", count)
print("Avg:", round(average, 2))