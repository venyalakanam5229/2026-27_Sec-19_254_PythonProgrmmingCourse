def shopping_cart(**products):
    total = 0
    print("Items Purchased:")
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total += price
    print(f"Total: ₹{total}")
shopping_cart(avocado=100, star_fruit=199, mango=150)
