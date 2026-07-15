
class ProductManager:
    def __init__(self,filemanager):
        self.filemanager=filemanager
        self.products = self.filemanager.load_json("products.json")

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
      self.filemanager.save_json("products.json",self.products)
    def add_product(self, name, price):
       new_product_id = max(map(int, self.products.keys()), default=0) + 1
       self.products[str(new_product_id)]={
          "name":name,
          "price":price
       }
       self.save_products()
    def update_product(self,product_id,name,price):
       if not self.is_valid_product(product_id):
          return "product id not exist"
       product=self.get_product(product_id)
       product["name"]=name
       product["price"]=price
       self.save_products()
       return "updated product"
    def delete_product(self,product_id):
       if not self.is_valid_product(product_id):
          return "product id not exist"
       
       del self.products[str(product_id)]
       self.save_products()
       return "product deleted "
       
       

          

