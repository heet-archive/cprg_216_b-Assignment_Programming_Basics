"""
  Class: CPRG216-B
  Author_Name: Group-9 (Heet Kartik Talati, Brett Shalagan, Chidera Mbama)
  Desc: 
  Assignment: Programming Basics
  Version: 30-September-2024
"""

# Import statements
from typing import Final

#Constants
GAS_PRICE:Final = 1.05
OIL_PRICE:Final = 1.25
LITRES_PER_CASE:Final = 12

# Printing select statements
print('-'*44)
print("*** Welcome to Gas Station Program ***")
print('-'*44)

print("Please select the type of purchase:")
print("G: Gas")
print("O: Oil")

purchase_type = input(">>> ")

# Assigning the product type and taking quantity input
if purchase_type == "G" or purchase_type == 'g':
    oil_gas_check = False
    product = "Gas"
    QUANTITY:Final = float(input("Enter the number of litres of gas: "))
elif purchase_type == 'O' or purchase_type == 'o':
    oil_gas_check = True
    product = "Oil"
    QUANTITY:Final = float(input("Enter # of cases of oil: "))
else:
    print("Invalid input, you should enter g/G or o/O")
    exit()

# Checking if the input quantity is valid
if QUANTITY <= 0:
  if oil_gas_check: #If oil
    print("Number of oil cases should be > 0")
    exit()
  if oil_gas_check == False: #If gas
    print("Number of gas litres should be > 0")
    exit()
else:
  # Assigning GST according to the province input
  province = input("Please enter the 2 letters province abbreviation: ")

  match province:
    case "AB" | "ab" | "BC" | "bc" | "MB" | "mb" | "NT" | "nt" | "NU" | "nu" | "QC" | "qc" | "SK" | "sk" | "YT" | "yt":
      gst = 5/100
    case "ON" | "on":
      gst = 13/100
    case _:
      gst = 15/100

# Assigning applicable discount on the selected product
if oil_gas_check and QUANTITY > 6:
  discount = 10/100 #percent discount
elif oil_gas_check == False and QUANTITY > 2000:
  discount = 10/100
else:
  discount = 0

# Calculate cost based on the quantity of product
if oil_gas_check: #for oil
  num_litres = QUANTITY * LITRES_PER_CASE 
  original_price = num_litres * OIL_PRICE
else: #for gas
  num_litres = QUANTITY
  original_price = num_litres * GAS_PRICE

# Applying discount and GST
final_price = original_price * (1 - discount)
total_gst = final_price * gst
final_price_after_gst = final_price + total_gst

# Printing the final output table
print('-'*100)
print(format('Product', '10s'), format('# Of Litres', '15s'), format('Price Before Discount', '25s'), format('Price After Discount', '24s'), format('GST', '7s'), 'Total Price')
print(format(f'{product:^8}', '10s'), format(f'{QUANTITY:^13}', '15s'), format(f'{original_price:^23}', '25s'), format(f'{final_price:^22}', '24s'), format(f'{total_gst:^5}', '7s'), f'{final_price_after_gst:^12}')
print('-'*100)

print("Thanks for your business, Good Bye")
