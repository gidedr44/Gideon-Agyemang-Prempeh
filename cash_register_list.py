""" Purpose: Read an inventory file of groceries, prices and units
Then read a grocery list file and print a receipt from using both files

Author: Gideon Agyemang Prempeh.     Date: April 4, 2019"""
unit_dicts = {} 
price_dict = {}
price_file = open("grocery_store_price_list.txt", "r")
for line_str in price_file:
    line_str = line_str.strip()
    item_str, price_str, unit_dict = line_str.split()
    price_flt = float(price_str)
    price_dict[item_str] = price_flt
    unit_dicts[item_str] = unit_dict
price_file.close()

my_purchases = []
purchase_file = open("my_personal_gro_list.txt", "r")
for line_str in purchase_file:
    line_str = line_str.strip()
    qty_str, item_str = line_str.split()
    qty_int = int(qty_str)
    my_purchases.append( (qty_int, item_str) ) 

print( "  N  Qty item      Unit    Extension" )

purchase_file.close()
print(50*"-")
total_amount = 0
count = 0
for purchase in my_purchases:
    count += 1
    quantity = purchase[0]
    item     = purchase[1]
    unit_cost = price_dict[item]
    unit_of_item = unit_dicts[ item ]
    extension = quantity*unit_cost
    total_amount = total_amount + extension
    total_amount=round(total_amount, 2)
    print( "{:3d} {:3d} {:10s} {:6s} {:7.2f}".format(\
        count, quantity, item, unit_of_item, extension) )

print(50*"-")
round(total_amount, 2)
print(24*" ", "Total", total_amount)

