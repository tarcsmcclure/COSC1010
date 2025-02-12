#
# Anna McClure
# 2/11/2025
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations
purchase_amt = 0
sales_tax = 0
total_sale = 0



# Constants for the state and county tax rates
state_st = 0.05
county_st = 0.025

# Get the amount of the purchase.
purchase_amt = float(input("Enter the amount of the sale in dollars >>>"))

# Calculate the state sales tax.
purchase_amt * 0.05

# Calculate the county sales tax.
purchase_amt * 0.025

# Calculate the total tax.
sales_tax = float(purchase_amt * 0.05) + float(purchase_amt * 0.025)

# Calculate the total of the sale.
total_sale = float(sales_tax + purchase_amt)

# Print information about the sale.
print("The purchase price is $", format(purchase_amt, ',.2f'))
print("The state sales tax is $", format(state_st, ',.2f'))
print("The county sales tax is $", format(county_st, ',.2f'))
print("The total sale price is $", format(total_sale, ',.2f'))
