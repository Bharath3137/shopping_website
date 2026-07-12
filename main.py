products = {
    1:"laptop",
    2:"mobile"
    }

cart = {}

def view_products():
    for product_id,product in products.items():
       print(product_id,product)

def search_products(search_name):
   for product_id,product_name in products.items():
         if search_name.lower() == product_name.lower():
             return product_id,product_name
   return "not found"

def add_to_cart(product_id):
    if product_id not in products:
         return "invalid product_id"
    cart[product_id] = cart.get(product_id,0)+1

def view_cart():
    if not cart:
        print("cart is empty")
        return
    for product_id,quantity in cart.items():
        print(products[product_id],quantity)
         
print("1.view menu\n2.search products\n3.Add products to cart\n4View cart.\n5.Exit")
while True:
   print("1.view products\n2.search products\n3.Add products to cart\n4View cart.\n5.Exit")
   choice=int(input("enter your choice"))
   if choice == 1:
      view_products()
   elif choice == 2:
       search_name=input("Enter the product name")
       print(search_products(search_name))
   elif choice==3:
       product_id=int(input("enter product id"))
       print(add_to_cart(product_id))
   elif choice == 4:
       view_cart()
   elif choice == 5:
       print("thankyou")
       break
   else:
      print("please enter a valid input")

    