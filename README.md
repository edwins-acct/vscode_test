# Intro To Python: Week 4 Day 2

  ## Scenario
    - Similar to the week 3 inventory scenario. We are given the inventory for our stock and its time to place the order, before doing so we need to retrieve the unit price and calculate total price for each item and all items.

## Objectives
  - Using your newly learned Python skills, access the newly acquired company's vendors API to automate the task.

Before we play with the API, it would be best to see the workbook provided!
NOTE: also see what sheets are already provided and how they are named.

# Step 1:
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










