#The first bug I spotted was that the total was being replaced by each sale instead of adding all the sales together. The line used total = sale instead of total += sale. This helped me understand why it is important to read the code carefully and use print statements to check variable values. I am learning to look for what the code is doing differently from what I expect before immediately asking AI for help.
#The apply_discount(price, tier) function calculates a discounted price based on the customer's membership tier. Its inputs are price, which is the original price, and tier, which identifies the discount level. Gold customers receive 15% off, silver customers receive 10% off, bronze customers receive 5% off, and any other tier receives no discount. The function returns the final price after the discount. A colleague could use this function without reading its body if they knew what arguments to provide and understood that it returns the discounted price.
#I used ChatGPT to explain Python error messages and help me understand debugging concepts. I reviewed the explanations and made the code corrections myself. Using AI helped me understand what certain errors meant, but I realized that getting an explanation is not the same as solving the problem myself. I learn more when I try to identify the bug first and use AI to clarify concepts instead of relying on it to write the solution for me.

#Exercise 1: calculate_tax
def calculate_tax(price, rate):
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")
#Exercise 2: apply_discount
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
print(f"gold: ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none: ${apply_discount(200, 'none'):.2f}")
#Exercise 3: Compose them
discounted_price = apply_discount(200, 'gold')
print(f"After gold discount: ${discounted_price:.2f}")
tax = calculate_tax(discounted_price, 0.07)
print(f"Tax on discounted price at 7%: ${tax:.2f}")
price_with_tax = discounted_price + tax
print(f"After tax: ${price_with_tax:.2f}")
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax
print(f"final_price(200, 'gold', 0.07): ${final_price(200, 'gold', 0.07):.2f}")
#Exercise 4: Loop + Function
orders = [(200, 'gold'), (150, 'silver'), (100, 'bronze'), (50, 'none')]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price}, Tier: {tier}, Final: ${total:.2f}")
#Exercise 5: Debug First, Then Ask
sales = [120, 80, 250, 175, 90]
#Bug 1 fix: Add each sale to the running total instead of replacing the total with the current sale.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")
#Bug 2 fix: add the missing colon after the for statement
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")
#Bug 3 fix: Use < instead of <= so the index never reaches len(sales), which is outisde the list.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1
#Exercise 6: Scope experiment
x = 100 #global variable
def double_it():
    x = 999 # local variable, different from the global x
    return x * 2

print(x)
print(double_it())
print(x)
#Scope determines where a variable can be accessed
#A local variable belongs to a function while a global variable is defined outside a function.
#The output is 100, 1998, and 100. The first print statement displays 100 because x is a global variable. The function creates a separate local variable named x with the value 999, so double_it() returns 1998. The final print statement displays 100 again because changing the local variable inside the function does not change the global variable. Scope determines where variables can be accessed in a program.