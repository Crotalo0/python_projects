import coffee_shop

print("Welcome to",coffee_shop.shop_name)
print("Available sizes:", coffee_shop.coffee_sizes)
print("Available_roasts:",coffee_shop.coffee_roasts)

order_size=input("Size:")
roast_size=input("Roast:")

shop_says = coffee_shop.order_coffee(order_size, roast_size)
print(shop_says)

add_milk_response = input("Do you want milk? (y/n): ")
if "y" in add_milk_response.lower():
	milk_fat = input("What percent milk do you want added? ")
	shop_says = coffee_shop.add_milk_please(milk_fat)
	print(shop_says)

# They better give a tip...
print("THAT'S GOOD COFFEE!  Very good.  Your brain is working again.")
print("You better give a tip.")
tip_amount = input("Tip amount? ")
coffee_shop.give_tip(tip_amount)
