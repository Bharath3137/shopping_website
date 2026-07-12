products = {
    1:{"name":"laptop",
       "price":90000,
      },
    2:{"name":"mobile",
       "price":70000},
    }

cart = {}

def view_products():
    for product_id,product in products.items():
       print(f"ID: {product_id}\nProduct Name: {product['name']}\nPrice: ₹{product['price']}")

def search_products(search_name):
   for product_id,product in products.items():
         if search_name.lower() == product["name"].lower():
             return product_id,product
   return "not found"

def add_to_cart(product_id):
    if product_id not in products:
         return "invalid product_id"
    cart[product_id] = cart.get(product_id,0)+1
    return "product added successfuly"

def view_cart():
    if not cart:
        print("cart is empty")
        return
    for product_id,quantity in cart.items():
        print(products[product_id]["name"],quantity)

def remove_item_from_cart(product_id):
        if product_id not in cart:
             return "product not in cart"
        cart[product_id]-=1
        if cart[product_id]==0:
             del cart[product_id]
        return "sucessfully removed "
def checkout():
    if not cart:
        print("empty cart")
        return
    total_amount=0
    for product_id,quantity in cart.items():
         name = products[product_id]["name"]
         price = products[product_id]["price"]

         subtotal = price * quantity
         total_amount += subtotal

         print(f"{name} x {quantity} = ₹{subtotal}")
    print(f"Total Bill{total_amount}")
    print("thankyou")
    cart.clear()

      

while True:
   print("1.view menu\n2.search products\n3.Add products to cart\n4.View cart.\n5.remove item from cart\n6.checkout\n10.Exit")
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
   elif choice==5:
       product_id=int(input("enter the id of product"))
       print(remove_item_from_cart(product_id))
   elif choice==6:
       checkout()
   elif choice == 10:
       print("thankyou")
       break
   else:
      print("please enter a valid input")

