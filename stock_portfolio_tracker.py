STOCK_PRICES = {
    "Lays": 10,
    "Kurkure": 15,
    "Coke": 25,
    "Maggie": 30,
    "Maaza": 45
}

print("Available Stocks")
print("---------------------")
for stock, price in STOCK_PRICES.items():
    print(stock, ":", price)

grand_total = 0
bill = []

while True:
    stock = input("Enter the product name (or type 'exit' to finish): ").title()
    
    if stock == "Exit":
        break
        
    quantity = int(input("Enter the quantity: "))
    
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue
    
    if stock in STOCK_PRICES:
        total_price = STOCK_PRICES[stock] * quantity
        grand_total += total_price
        bill.append((stock, quantity, total_price))
        print("Total price for", quantity, stock, "is:", total_price)
    else:
        print("Sorry, the product is not available in stock.")

print("\n--- FINAL BILL ---")
for stock, quantity, total_price in bill:
    print(f"{stock:<10} x {quantity:<3} = ₹{total_price}")
print("------------------")
print("Grand Total:", grand_total)

with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("========== FINAL BILL ==========\n\n")
    for stock, quantity, total_price in bill:
        file.write(f"{stock:<10} x {quantity:<3} = ₹{total_price}\n")
    file.write("\n--------------------------------\n")
    file.write(f"Grand Total = ₹{grand_total}\n")

print("\nBill saved successfully to portfolio.txt")