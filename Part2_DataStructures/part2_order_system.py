#Task1:
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}
# Food items available in restaurant as per category
categories = []
for item in menu.values():
    if item["category"] not in categories:
        categories.append(item["category"])
# Printing menu grouped by category
for category in categories:
    print(f"\n===== {category} =====")    
    for name, details in menu.items():
        if details["category"] == category:
            price = details["price"]
            status = "Available" if details["available"] else "Unavailable"
            
            print(f"{name} ₹{price:.2f}   [{status}]")
# Total number of items
total_items = len(menu)
# Total available items
available_items = sum(1 for item in menu.values() if item["available"])
# Highest priced item
most_exp_item = max(menu.items(), key=lambda x: x[1]["price"])
most_exp_name = most_exp_item[0]
most_exp_price = most_exp_item[1]["price"]
# Items under ₹150
affordable_items = [(name, details["price"]) 
               for name, details in menu.items() 
               if details["price"] < 150]
# results
print("\n\n===== Summary =====")
print("Total items on menu      :", total_items)
print("Available items          :", available_items)
print(f"Most expensive item      : {most_exp_name} (₹{most_exp_price:.2f})")
print("Items under ₹150:")
for name, price in affordable_items:
    print(f"{name} - ₹{price:.2f}")
    

#Task2:
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},

    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}
cart = []
# checking  item
def add_to_cart(item_name, qty):
    if item_name not in menu:
        print(f"{item_name} not found in menu")
        return  
    if not menu[item_name]["available"]:
        print(f"{item_name} is currently unavailable")
        return
    # Checking if item already available
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += qty
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return
    # Adding new item
    cart.append({
        "item": item_name,
        "quantity": qty,
        "price": menu[item_name]["price"]
    })
    print(f"Added {item_name} x{qty}")
# remove item
def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f" Removed {item_name}")
            return
    print(f" {item_name} not found in cart")
# print item in cart
def print_cart():
    print("Current Cart:")
    for item in cart:
        print(item)      
#code for adding item
add_to_cart("Paneer Tikka", 2)
add_to_cart("Gulab Jamun", 1)
add_to_cart("Paneer Tikka", 1) 
add_to_cart("Mystery Burger", 1)  
add_to_cart("Chicken Wings", 1)  
print_cart()
remove_from_cart("Gulab Jamun")
print_cart()
# Final Order Summary
print("\n========== Order Summary ==========")
subtotal = 0
for item in cart:
    total_price = item["quantity"] * item["price"]
    subtotal += total_price
    print(f"{item['item']} x{item['quantity']}    ₹{total_price:.2f}")
gst = subtotal * 0.05
total = subtotal + gst
print("------------------------------------")
print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):                ₹{gst:.2f}")
print(f"Total Payable:           ₹{total:.2f}")
print("====================================")

#Task3:
import copy
inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}
#Deep copy
inventory_backup = copy.deepcopy(inventory) # original remains even if we change inventory_backup 
inventory["Paneer Tikka"]["stock"] = 5
print("Modified Inventory:")
print(inventory["Paneer Tikka"])
print("\nBackup Inventory  unchanged:")
print(inventory_backup["Paneer Tikka"])
# Restore original inventory
inventory = copy.deepcopy(inventory_backup)
# Final cart
cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0}
]
#Displaying inventory as per live data
print("\n===== Order Fulfilment =====")
for product in cart:
    item = product["item"]
    qty = product["quantity"]
    if item in inventory:
        available_stock = inventory[item]["stock"]

        if qty <= available_stock:
            inventory[item]["stock"] -= qty
            print(f" {item}: Deducted {qty}, Remaining {inventory[item]['stock']}")
        else:
            print(f"Not enough stock for {item}. Only {available_stock} available.")
            inventory[item]["stock"] = 0
#Threshold alerts
print("\n===== Reorder Alerts =====")
for item, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"Reorder Alert: {item} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")
#Final output
print("\n===== Final Inventory =====")
for item, details in inventory.items():
    print(f"{item} | Stock: {details['stock']} | Reorder Level: {details['reorder_level']}")
print("\n===== Backup Inventory =====")
for item, details in inventory_backup.items():
    print(f"{item} | Stock: {details['stock']} | Reorder Level: {details['reorder_level']}")
    
#Task4:
sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}
#print revenue per day and highest sales
def revenue_report(sales_log):
    print("\n===== Revenue Per Day =====")
    
    revenue_per_day = {}
    
    for date, orders in sales_log.items():
        total = sum(item["total"] for item in orders)
        revenue_per_day[date] = total
        print(f"{date} -> ₹{total:.2f}")
    
    best_day = max(revenue_per_day, key=revenue_per_day.get)
    print(f"\nBest Selling Day: {best_day} (₹{revenue_per_day[best_day]:.2f})")
    
    return revenue_per_day
#Initial revenue report
revenue_report(sales_log)
#Most ordered item
item_count = {}
for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)
print(f"\nMost Ordered Item: {most_ordered} ({item_count[most_ordered]} orders)")
# Adding new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]
#Updated revenue report
revenue_report(sales_log)

#list of all orders
print("\n===== All Orders =====")
all_orders = []
for date, orders in sales_log.items():
    for order in orders:
        all_orders.append((date, order))
for i, (date, order) in enumerate(all_orders, start=1):
    items_str = ", ".join(order["items"])
    print(f"{i}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items_str}")
