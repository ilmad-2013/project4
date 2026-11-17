
print("================================")
print("     SHOPPING DISCOUNT CALCULATOR")
print("================================")

items = []
prices = []
total = 0
total_saved = 0

number = int(input("How many items are you buying? "))

for i in range(number):
    print("\nItem", i + 1)

    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    discount = float(input("Enter discount percentage: "))

    if price < 0 or discount < 0 or discount > 100:
        print("Invalid price or discount. Try again.")
        continue

    saved = price * discount / 100
    final_price = price - saved

    items.append(name)
    prices.append(final_price)

    total += final_price
    total_saved += saved

    print("Money saved:", round(saved, 2))
    print("Final price:", round(final_price, 2))

print("\n========== SHOPPING RECEIPT ==========")

for i in range(len(items)):
    print(items[i], ":", round(prices[i], 2))

print("--------------------------------------")
print("Total items:", len(items))
print("Total spending:", round(total, 2))
print("Total savings:", round(total_saved, 2))

print("Thank you for shopping!")

