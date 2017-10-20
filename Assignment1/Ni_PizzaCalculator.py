__author__ = 'cni12345'

# A program that calculates the amount of pizza

'''
Cost to buy a pizza:
Veggie Pizza = $16.00
Meat-Lover Pizza = $18.00
Cheese Pizza = $12.00

Cost for ingredients per pizza
Dough and Sauce = $5.00
Veggie = $3.00
Meat = $6.00
Cheese = $2.00
'''

veggiesSold = int(input('How many vegetarian pizzas were sold last week? '))
meatSold = int(input('How many meat pizzas were sold last week?'))
cheeseSold = int(input('How many cheese pizzas were sold last week? '))

# Total spent per week to buy pizza ingredient
avgSpent = (600 * 5.00) + (250 * 3.00) + (250 * 6.00) + (100 * 2.00)

# Total dollar amount made from pizza sales
totalSales = (16.00 * veggiesSold) + (18.00 * meatSold) + (12.00 * cheeseSold)

# Profit or loss for the pass week
profitOrLoss = totalSales - avgSpent

# Cost of food wasted
wasted = ((600 * 5.00) - ((veggiesSold + meatSold + cheeseSold) * 5)) + \
         ((250 * 3.00) - (veggiesSold * 3.00)) + ((250 * 6.00) -
                                                  (meatSold * 6.00)) + ((100 * 2.00) - (cheeseSold * 2.00))

print('How many vegetarian pizzas were sold last week?', veggiesSold)
print('How many meat-lover pizzas were sold last week?', meatSold)
print('How many cheese pizzas were sold last week?', cheeseSold)
print('Amount spent on pizza ingredients: $', end='')
print("%.2f" % avgSpent)
print('Amount of pizza sales: $', end='')
print("%.2f" % totalSales)
print('Profit (or loss, if negative): $', end='')
print("%.2f" % profitOrLoss)
print('Cost of food wasted (unused pizza ingredients): $', end='')
print("%.2f" % wasted)
