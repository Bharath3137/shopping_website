from databasemanager import DatabaseManager
from productmanager import ProductManager
from cartmanager import CartManager
from user import UserManager
from dashboardmanager import DashboardManager
from utils import get_int, get_float, display_products

databasemanager = DatabaseManager()
dashboardmanager = DashboardManager(databasemanager)
productmanager = ProductManager(databasemanager)
usermanager = UserManager(databasemanager)
cartmanager = CartManager(productmanager, databasemanager, usermanager)


def customer_menu():

    while True:

        print("\n===== Customer Menu =====")
        print("1. View Products")
        print("2. Search Products")
        print("3. Add To Cart")
        print("4. View Cart")
        print("5. Remove Item From Cart")
        print("6. Checkout")
        print("7. view orders")
        print("8.Logout")

        customer_choice = get_int("Enter your choice: ")

        if customer_choice == 1:

            products = productmanager.get_all_products()

            display_products(products)

        elif customer_choice == 2:

            name = input("Enter Product Name: ")

            products = productmanager.search_product(name)

            display_products(products)

        elif customer_choice == 3:

            product_id = get_int("Enter Product ID: ")
            print(cartmanager.add_to_cart(product_id))

        elif customer_choice == 4:

            cartmanager.view_cart()

        elif customer_choice == 5:

            product_id = get_int("Enter Product ID: ")
            print(cartmanager.remove_item_from_cart(product_id))

        elif customer_choice == 6:

            print(cartmanager.checkout())

        elif customer_choice == 7:
            cartmanager.view_order_history()

        elif customer_choice == 8:

            print(usermanager.logout())
            break

        else:

            print("Invalid Choice")


def admin_menu():

    while True:

        print("\n===== Admin Menu =====")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Dashboard")
        print("6. Logout")

        admin_choice = get_int("Enter your choice: ")

        if admin_choice == 1:

            products = productmanager.get_all_products()

            display_products(products)
        elif admin_choice == 2:

            name = input("Enter Product Name: ")
            price = get_float("Enter Product Price: ")
            stock = get_int("Enter Product Stock: ")
            category = input("Enter Product Category: ")

            print(productmanager.add_product(name, price, stock, category))

        elif admin_choice == 3:

            product_id = get_int("Enter Product ID: ")

            print("\n1. Name")
            print("2. Price")
            print("3. Stock")
            print("4. Category")

            choice = get_int("Choose Field: ")

            fields = {1: "name", 2: "price", 3: "stock", 4: "category"}

            if choice not in fields:
                print("Invalid Choice")

            else:

                value = input("Enter New Value: ")

                if choice == 2:
                    value = float(value)

                elif choice == 3:
                    value = int(value)

                print(productmanager.update_product(product_id, fields[choice], value))
        elif admin_choice == 4:

            product_id = get_int("Enter Product ID: ")
            print(productmanager.delete_product(product_id))
        elif admin_choice == 5:

            dashboard = dashboardmanager.get_dashboard()

            print("\n========== ADMIN DASHBOARD ==========")
            print(f"Total Users    : {dashboard['total_users']}")
            print(f"Total Products : {dashboard['total_products']}")
            print(f"Total Orders   : {dashboard['total_orders']}")
            print(f"Total Revenue  : ₹{dashboard['total_revenue']}")
            print("\nTop Selling Products")
            print("------------------------------")

            for product in dashboard["top_products"]:

                print(f"{product['name']} - {product['sold']} Sold")

        elif admin_choice == 6:

            print(usermanager.logout())
            break

        else:

            print("Invalid Choice")


while True:

    print("\n===== Shopping Management System =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = get_int("Enter your choice: ")

    if choice == 1:

        username = input("Enter Username: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        print(usermanager.register_user(username, email, password))

    elif choice == 2:

        email = input("Enter Email: ")
        password = input("Enter Password: ")

        result = usermanager.login_user(email, password)

        print(result)

        if result == "Login Successful":

            user = usermanager.get_current_user()

            if user["role"] == "Admin":

                admin_menu()

            else:

                customer_menu()

    elif choice == 3:

        databasemanager.close()
        print("Thank You!")
        break

    else:

        print("Invalid Choice")
