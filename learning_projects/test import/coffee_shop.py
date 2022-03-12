# Imposto delle variabili che verranno richiamate nel programma madre

shop_name = "Congo Coffee Shop"
coffee_sizes = ["small","medium","large","gigantic"]
coffee_roasts =["hot chocolate", "light", "medium", "dark", "espresso"] 

def order_coffee(size, roast):
	return "Here's your coffee {} roasted {}".format(size,roast)

def add_milk_please(fat_content):
	return "I've added the {}% milk".format(fat_content)

def give_tip(tip_amount):
	print("Thank you!")
