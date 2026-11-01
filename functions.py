#1. the first bug i spotted was the missing colon on the second for
#loop, bc python gave a SyntaxError pointing right at it. the
#    hardest one to find was "total = sale" bc it ran with no error
#    and just printed the wrong total (90), so i had to trace it
#    through with print statements.
#
# 2. apply_discount(price, tier) takes a price (a number) and a
#    tier (a string like "gold", "silver", "bronze"). it looks at
#    the tier, takes 15% off for gold, 10% off for silver, 5% off
#    for bronze, and nothing for anything else. it returns the new
#    discounted price. a coworker could use it without reading the
#    body bc they just need to know what goes in and what comes out.
#
# 3. AI disclosure: I used claude throughout exercise #5 
# were the exercised ask me I did not use it anywhere eles


# Exercise 1

# Define calcutate tax fuction

def calculate_tax(price, rate):
    return price * rate 

#Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tac on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")

#Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
    
 # calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers: 
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

discounted = apply_discount(200,"gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(100, "gold"), (150, "sliver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final : ${total:.2f}")

# --- Exercise 5 ---
# Bugs found in broken_sales.py:
# Bug 1 (logic error): "total = sale" overwrote total every loop, so
#   it only ever held the last sale (90). fixed with "total += sale".
# Bug 2 (syntax error): the second for loop was missing its colon.
#   python points right at it with a SyntaxError.
# Bug 3 (index error): "while i <= len(sales)" runs one time too many.
#   the list has 5 items (index 0-4) so when i = 5 sales[5] crashes
#   with IndexError. fixed by changing <= to <.
# Step 4: the AI explanation [matched / did not match] what i found.
#   [EDIT: write what actually happened]

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Exerise 6

x = 100 
def double_it():
     global x
     return x * 2

print(x) 
print (double_it())
print(x)