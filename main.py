from products import ProductManager
from cart import CartManager
from file_manager import FileManager
filemanager=FileManager()
productmanager=ProductManager(filemanager)
cartmanager=CartManager(productmanager,filemanager)


while True:
    print("===== Shopping Management System =====\n"
          "1. Customer\n"
          "2. Admin\n"
          "3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        while True:
            print("===== Customer Menu =====\n"
                  "1. View Products\n"
                  "2. Search Products\n"
                  "3. Add to Cart\n"
                  "4. View Cart\n"
                  "5. Remove Item from Cart\n"
                  "6. Checkout\n"
                  "7. Back")

            customer_choice = int(input("Enter your choice: "))

            if customer_choice == 1:
                productmanager.view_products()

            elif customer_choice == 2:
                search_name = input("Enter product name: ")
                product = productmanager.search_products(search_name)

                if product:
                    print(product)
                else:
                    print("Product not found")

            elif customer_choice == 3:
                product_id = int(input("Enter Product ID: "))
                print(cartmanager.add_to_cart(product_id))

            elif customer_choice == 4:
                cartmanager.view_cart()

            elif customer_choice == 5:
                product_id = int(input("Enter Product ID: "))
                print(cartmanager.remove_item_from_cart(product_id))

            elif customer_choice == 6:
                cartmanager.checkout()

            elif customer_choice == 7:
                break

            else:
                print("Invalid choice")

    elif choice == 2:
        while True:
            print("===== Admin Menu =====\n"
                  "1. View Products\n"
                  "2. Add Product\n"
                  "3. Update Product\n"
                  "4. Delete Product\n"
                  "5. Back")

            admin_choice = int(input("Enter your choice: "))

            if admin_choice == 1:
                productmanager.view_products()

            elif admin_choice == 2:
                name = input("Enter Product Name: ")
                price = int(input("Enter Product Price: "))
                print(productmanager.add_product(name, price))

            elif admin_choice == 3:
                product_id = int(input("Enter Product ID: "))

                print("1. Update Name\n"
                      "2. Update Price\n"
                      "3. Update Both")

                update_choice = int(input("Enter your choice: "))

                if update_choice == 1:
                    name = input("Enter New Name: ")
                    print(productmanager.update_product(product_id, name=name))

                elif update_choice == 2:
                    price = int(input("Enter New Price: "))
                    print(productmanager.update_product(product_id, price=price))

                elif update_choice == 3:
                    name = input("Enter New Name: ")
                    price = int(input("Enter New Price: "))
                    print(productmanager.update_product(product_id, name, price))

                else:
                    print("Invalid choice")

            elif admin_choice == 4:
                product_id = int(input("Enter Product ID: "))
                print(productmanager.delete_product(product_id))

            elif admin_choice == 5:
                break

            else:
                print("Invalid choice")

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice")