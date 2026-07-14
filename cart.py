import json
class CartManager:
   def __init__(self,productmanager):
       self.productmanager=productmanager
       try:
        with open("cart.json","r") as file:
           self.cart=json.load(file)
       except FileNotFoundError:
          self.cart={}
       
       

   def view_cart(self):
     if not self.cart:
        print("cart is empty")
        return
     for product_id,quantity in self.cart.items():
        print( self.productmanager.get_product(product_id)["name"],quantity)
   
   def save_cart(self):
       with open("cart.json","w") as file:
           json.dump(self.cart,file,indent=4)

   def add_to_cart(self,product_id):
     if not self.productmanager.is_valid_product(product_id):
         return "invalid product_id"
     self.cart[str(product_id)]=self.cart.get(str(product_id),0)+1
     self.save_cart()
     return "product added successfuly"
     

   def remove_item_from_cart(self,product_id):
        if str(product_id) not in self.cart:
             return "product not in cart"
        self.cart[str(product_id)]-=1
        if self.cart[str(product_id)]==0:
             del self.cart[str(product_id)]
        self.save_cart()
        return "sucessfully removed "

   def checkout(self):
    if not self.cart:
        print("empty cart")
        return
    total_amount=0
    for product_id,quantity in self.cart.items():
         product= self.productmanager.get_product(product_id)
         
         name=product["name"]
         price=product["price"]
         subtotal = price * quantity
         total_amount += subtotal

         print(f"{name} x {quantity} = ₹{subtotal}")
    print(f"Total Bill{total_amount}")
    print("thankyou")
    self.cart.clear()