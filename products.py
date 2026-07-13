products = {
    1:{"name":"laptop",
       "price":90000,
      },
    2:{"name":"mobile",
       "price":70000},
    }



def view_products():
    for product_id,product in products.items():
       print(f"ID: {product_id}\nProduct Name: {product['name']}\nPrice: ₹{product['price']}")

def search_products(search_name):
   for product_id,product in products.items():
         if search_name.lower() == product["name"].lower():
             return product_id,product
   return "not found"

