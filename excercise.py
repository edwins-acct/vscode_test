'''# Step 1:
We need to populate the order_list with the products that are below the reorder threshold.
If the product requires reorder than move it from inventory_list to order_list.

Note: order_list only requires (Product id, Vendor, Product Name, Order Amount from the inventory_list)

# Step 2
Base_url = https://vit-py-api.herokuapp.com/

Working only inside the order_list take the Base url/{vendor}/{product_id} to retrieve the price for each product.
  - Make sure that you are familiar with how the model schema from the API is set up.
  - You must calculate the total price for each product, since you are only given the unit price from the API(total_price = unit_price * reorder_amount).
  
  Note: you can do this immediately after making the API call or retrieve all the unit prices first and then perform the calculations.
  
# Step 3
Once you have all the data populated into the order_list worksheet, we will need a cost for the total order.
  - Calculate total price for this order. Append this to a new row.
'''

import requests,json, openpyxl, sys
print(sys.executable)
print(sys.version)
sys.exit()

base_url = 'https://vit-py-api.herokuapp.com/'

wb = openpyxl.load_workbook('./main_company_inventory.xlsx')
ws_inventory = wb['inventory_list']
ws_order = wb['order_list']
count = 2
for row_num, (id,prod_name, qty_stock, reorder_bool, threshold, reorder_amt, vendor, prod_desc) in enumerate(ws_inventory.iter_rows(),1):
  # print(type(row_inventory))
  print(row_inventory[0].value)
  if row_num == 1:
      continue
  response = requests.get(base_url + vendor.value + '/'+ id.value)
  data = response.json()
  if str(reorder_bool.value) == 'True':
      total_price = reorder_amt.value * data['unit_price']
      order_amt = reorder_amt.value 


sys.exit()
# for row_num, (id,prod_name, qty_stock, reorder_bool, threshold, reorder_amt, vendor, prod_desc) in enumerate(ws_inventory.iter_rows(),1):
#     if row_num == 1:
#         continue
#     response = requests.get(base_url + vendor.value + '/'+ id.value)
#     data = response.json()
#     if str(reorder_bool.value) == 'True':
#         total_price = reorder_amt.value * data['unit_price']
#         order_amt = reorder_amt.value 
#         # print(total_price, order_amt)
#         for row in 
#         ws_order.cell(row=count, column=1, value= str(id.value))
#         ws_order.cell(row=count, column=2, value= str(vendor.value))
#         count +=1

# wb.save('./main_company_inventory.xlsx')
    # print(data)

r = requests.get
