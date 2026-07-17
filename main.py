from databasemanager import DatabaseManager
from products import ProductManager
from cart import CartManager

databasemanager = DatabaseManager()
productmanager = ProductManager(databasemanager)
cartmanager = CartManager(productmanager, databasemanager)

while True:

    print("\n===== Shopping Management System =====")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        while True:

            print("\n===== Customer Menu =====")
            print("1. View Products")
            print("2. Search Products")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Remove Item from Cart")
            print("6. Checkout")
            print("7. Back")

            customer_choice = int(input("Enter your choice: "))

            if customer_choice == 1:

                products = productmanager.get_all_products()

                if not products:
                    print("No Products Available")

                else:
                    for product in products:
                        print("---------------------------")
                        print(f"ID       : {product['id']}")
                        print(f"Name     : {product['name']}")
                        print(f"Price    : ₹{product['price']}")
                        print(f"Stock    : {product['stock']}")
                        print(f"Category : {product['category']}")
                        print("---------------------------")

            elif customer_choice == 2:

                name = input("Enter Product Name: ")

                products = productmanager.search_product(name)

                if not products:
                    print("Product Not Found")

                else:
                    for product in products:
                        print("---------------------------")
                        print(f"ID       : {product['id']}")
                        print(f"Name     : {product['name']}")
                        print(f"Price    : ₹{product['price']}")
                        print(f"Stock    : {product['stock']}")
                        print(f"Category : {product['category']}")
                        print("---------------------------")

            elif customer_choice == 3:

                product_id = int(input("Enter Product ID: "))
                print(cartmanager.add_to_cart(product_id))

            elif customer_choice == 4:

                cartmanager.view_cart()

            elif customer_choice == 5:

                product_id = int(input("Enter Product ID: "))
                print(cartmanager.remove_item_from_cart(product_id))

            elif customer_choice == 6:

                print(cartmanager.checkout())

            elif customer_choice == 7:
                break

            else:
                print("Invalid Choice")

    elif choice == 2:

        while True:

            print("\n===== Admin Menu =====")
            print("1. View Products")
            print("2. Add Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Back")

            admin_choice = int(input("Enter your choice: "))

            if admin_choice == 1:

                products = productmanager.get_all_products()

                if not products:
                    print("No Products Available")

                else:
                    for product in products:
                        print("---------------------------")
                        print(f"ID       : {product['id']}")
                        print(f"Name     : {product['name']}")
                        print(f"Price    : ₹{product['price']}")
                        print(f"Stock    : {product['stock']}")
                        print(f"Category : {product['category']}")
                        print("---------------------------")

            elif admin_choice == 2:

                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Product Stock: "))
                category = input("Enter Product Category: ")

                print(productmanager.add_product(name, price, stock, category))

            elif admin_choice == 3:

                product_id = int(input("Enter Product ID: "))

                print("\n1. Name")
                print("2. Price")
                print("3. Stock")
                print("4. Category")

                choice = int(input("Choose Field: "))

                fields = {
                    1: "name",
                    2: "price",
                    3: "stock",
                    4: "category"
                }

                if choice not in fields:
                    print("Invalid Choice")

                else:

                    value = input("Enter New Value: ")

                    if choice == 2:
                        value = float(value)

                    elif choice == 3:
                        value = int(value)

                    print(
                        productmanager.update_product(
                            product_id,
                            fields[choice],
                            value
                        )
                    )

            elif admin_choice == 4:

                product_id = int(input("Enter Product ID: "))
                print(productmanager.delete_product(product_id))

            elif admin_choice == 5:
                break

            else:
                print("Invalid Choice")

    elif choice == 3:

        databasemanager.close()
        print("Thank You!")
        break

    else:
        print("Invalid Choice")