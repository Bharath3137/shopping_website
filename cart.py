class CartManager:

    def __init__(self, productmanager, databasemanager):
        self.productmanager = productmanager
        self.databasemanager = databasemanager
        self.user_id = 1

    def add_to_cart(self, product_id):

        if not self.productmanager.is_valid_product(product_id):
            return "Invalid Product ID"

        query = f"""
        SELECT * FROM cart
        WHERE user_id={self.user_id}
        AND product_id={product_id}
        """

        cart_item = self.databasemanager.execute_query(query)

        if cart_item:

            quantity = cart_item[0]["quantity"] + 1

            query = f"""
            UPDATE cart
            SET quantity={quantity}
            WHERE user_id={self.user_id}
            AND product_id={product_id}
            """

        else:

            query = f"""
            INSERT INTO cart(user_id, product_id, quantity)
            VALUES({self.user_id}, {product_id}, 1)
            """

        self.databasemanager.execute_query(query)

        return "Product Added Successfully"

    def view_cart(self):

        query = f"""
        SELECT
            products.name,
            products.price,
            cart.quantity
        FROM cart
        JOIN products
        ON cart.product_id = products.id
        WHERE cart.user_id={self.user_id}
        """

        items = self.databasemanager.execute_query(query)

        if not items:
            print("Cart is Empty")
            return

        total = 0

        for item in items:

            subtotal = item["price"] * item["quantity"]
            total += subtotal

            print(
                f"{item['name']} "
                f"x{item['quantity']} "
                f"= ₹{subtotal}"
            )

        print(f"\nTotal = ₹{total}")

    def remove_item_from_cart(self, product_id):

        query = f"""
        SELECT * FROM cart
        WHERE user_id={self.user_id}
        AND product_id={product_id}
        """

        item = self.databasemanager.execute_query(query)

        if not item:
            return "Product Not Found In Cart"

        quantity = item[0]["quantity"]

        if quantity > 1:

            query = f"""
            UPDATE cart
            SET quantity={quantity-1}
            WHERE user_id={self.user_id}
            AND product_id={product_id}
            """

        else:

            query = f"""
            DELETE FROM cart
            WHERE user_id={self.user_id}
            AND product_id={product_id}
            """

        self.databasemanager.execute_query(query)

        return "Removed Successfully"

    def checkout(self):

       query = f"""
       SELECT
        cart.product_id,
        cart.quantity,
        products.price,
        products.stock
       FROM cart
       JOIN products
       ON cart.product_id = products.id
       WHERE cart.user_id = {self.user_id}
       """

       cart_items = self.databasemanager.execute_query(query)

       if not cart_items:
          return "Cart is Empty"

       total_amount = 0

       for item in cart_items:

          if item["quantity"] > item["stock"]:
            return f"Not enough stock for Product ID {item['product_id']}"

          total_amount += item["price"] * item["quantity"]

       query = f"""
       INSERT INTO orders(user_id, total_amount)
       VALUES({self.user_id}, {total_amount})
       """

       order_id = self.databasemanager.execute_insert(query)

       for item in cart_items:

          query = f"""
          INSERT INTO order_items(order_id, product_id, quantity, price)
          VALUES(
             {order_id},
             {item['product_id']},
             {item['quantity']},
             {item['price']}
          )
          """

          self.databasemanager.execute_query(query)

          query = f"""
          UPDATE products
          SET stock = stock - {item['quantity']}
          WHERE id = {item['product_id']}
          """

          self.databasemanager.execute_query(query)

       query = f"""
       DELETE FROM cart
       WHERE user_id = {self.user_id}
       """

       self.databasemanager.execute_query(query)

       return f"Order Placed Successfully! Total = ₹{total_amount}"