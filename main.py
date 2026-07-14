from products import ProductManager
from cart import CartManager
productmanager=ProductManager()
cartmanager=CartManager(productmanager)


while True:
   print("1.view menu\n2.search products\n3.Add products to cart\n4.View cart.\n5.remove item from cart\n6.checkout\n10.Exit")
   choice=int(input("enter your choice"))
   if choice == 1:
      productmanager.view_products()
   elif choice == 2:
    search_name = input("Enter the product name")
    product = productmanager.search_products(search_name)

    if product:
        print(product)
    else:
        print("Product not found")
   elif choice==3:
       product_id=int(input("enter product id"))
       print(cartmanager.add_to_cart(product_id))
   elif choice == 4:
       cartmanager.view_cart()
   elif choice==5:
       product_id=int(input("enter the id of product"))
       print(cartmanager.remove_item_from_cart(product_id))
   elif choice==6:
       cartmanager.checkout()

   elif choice == 10:
       print("thankyou")
       break
   else:
      print("please enter a valid input")

