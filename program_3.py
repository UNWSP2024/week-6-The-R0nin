# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:
Sales_Tax = 0.05
Country_Sales_Tax = 0.025

monthy_sale = float(input('List sale for the month: $'))

sales_price = monthy_sale * Sales_Tax
country_sales_price = monthy_sale * Country_Sales_Tax
total = sales_price + country_sales_price

print('With sales tax: $', float(sales_price))
print('With country sales tax: $', float(country_sales_price))
print('Total: $', float(total))

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
