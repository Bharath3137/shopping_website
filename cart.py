from products import products
cart = {}
def view_cart():
    if not cart:
        print("cart is empty")
        return
    for product_id,quantity in cart.items():
        print(products[product_id]["name"],quantity)

def add_to_cart(product_id):
    if product_id not in products:
         return "invalid product_id"
    cart[product_id] = cart.get(product_id,0)+1
    return "product added successfuly"

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