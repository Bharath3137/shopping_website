from products import products,view_products,search_products
from cart import cart,add_to_cart,remove_item_from_cart,view_cart,checkout

      

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

