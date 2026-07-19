def get_int(message):

    while True:

        try:
            return int(input(message))

        except ValueError:
            print("Please enter a valid integer.")


def get_float(message):

    while True:

        try:
            return float(input(message))

        except ValueError:
            print("Please enter a valid number.")


def display_products(products):

    if not products:
        print("No Products Available")
        return

    for product in products:
        print("---------------------------")
        print(f"ID       : {product['id']}")
        print(f"Name     : {product['name']}")
        print(f"Price    : ₹{product['price']}")
        print(f"Stock    : {product['stock']}")
        print(f"Category : {product['category']}")
        print("---------------------------")
