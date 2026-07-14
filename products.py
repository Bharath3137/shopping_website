import json

class ProductManager:
    def __init__(self):
      try:
        with open("products.json", "r") as file:
            self.products = json.load(file)
      except FileNotFoundError:
         self.products={}

    def view_products(self):
      for product_id,product in self.products.items():
          print(f"ID: {product_id}\nProduct Name: {product['name']}\nPrice: ₹{product['price']}")

    def search_products(self,search_name):
       for product_id,product in self.products.items():
         if search_name.lower() == product["name"].lower():
             return product_id,product
       return None
    def is_valid_product(self,product_id):
     return str(product_id) in self.products
    
    def get_product(self,product_id):
      if str(product_id) in self.products:
         return self.products[str(product_id)]
      return None
    def save_products(self):
      with open("products.json", "w") as file:
        json.dump(self.products, file, indent=4)
    def add_product(self, name, price):
       new_product_id=len(self.products)+1
       self.products[str(new_product_id)]={
          "name":name,
          "price":price
       }
       self.save_products()


