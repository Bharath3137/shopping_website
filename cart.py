class CartManager:

    def __init__(self, productmanager, databasemanager):
        self.productmanager = productmanager
        self.databasemanager = databasemanager
        self.user_id = 1

    def add_to_cart(self, product_id):

        if not self.productmanager.is_valid_product(product_id):
            return "Invalid Product ID"

        query = """
        SELECT * FROM cart
        WHERE user_id=%s
        AND product_id=%s
        """

        cart_item = self.databasemanager.execute_query(query,(self.user_id,product_id))

        if cart_item:

            quantity = cart_item[0]["quantity"] + 1

            query = """
            UPDATE cart
            SET quantity=%s
            WHERE user_id=%s
            AND product_id=%s
            """
            self.databasemanager.execute_query(query,(quantity,self.user_id,product_id))

        else:

            query = """
            INSERT INTO cart(user_id, product_id, quantity)
            VALUES(%s,%s,%s)
            """

            self.databasemanager.execute_query(query,(self.user_id,product_id,1))

        return "Product Added Successfully"

    def view_cart(self):

        query = """
        SELECT
            products.name,
            products.price,
            cart.quantity
        FROM cart
        JOIN products
        ON cart.product_id = products.id
        WHERE cart.user_id=%s
        """

        items = self.databasemanager.execute_query(query,(self.user_id,))

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

        query = """
        SELECT * FROM cart
        WHERE user_id=%s
        AND product_id=%s
        """

        item = self.databasemanager.execute_query(query,(self.user_id,product_id))

        if not item:
            return "Product Not Found In Cart"

        quantity = item[0]["quantity"]

        if quantity > 1:

            query = """
            UPDATE cart
            SET quantity=%s
            WHERE user_id=%s
            AND product_id=%s
            """
            self.databasemanager.execute_query(query,(quantity-1,self.user_id,product_id))
        else:

            query = """
            DELETE FROM cart
            WHERE user_id=%s
            AND product_id=%s
            """

        self.databasemanager.execute_query(query,(self.user_id,product_id))

        return "Removed Successfully"

    def checkout(self):
      try:

       self.databasemanager.begin_transaction()

       query = """
       SELECT
        cart.product_id,
        cart.quantity,
        products.price,
        products.stock
       FROM cart
       JOIN products
       ON cart.product_id = products.id
       WHERE cart.user_id = %s
       """

       cart_items = self.databasemanager.execute_query(query,(self.user_id,))

       if not cart_items:
          return "Cart is Empty"

       total_amount = 0

       for item in cart_items:

          if item["quantity"] > item["stock"]:
            return f"Not enough stock for Product ID {item['product_id']}"

          total_amount += item["price"] * item["quantity"]

       query = """
       INSERT INTO orders(user_id, total_amount)
       VALUES(%s, %s)
       """

       order_id = self.databasemanager.execute_insert(query,(self.user_id,total_amount))

       for item in cart_items:

          query = """
          INSERT INTO order_items(order_id, product_id, quantity, price)
          VALUES(
            %s,%s,%s,%s
          )
          """
          
          self.databasemanager.execute_query(query,(order_id,item['product_id'],item['quantity'],item['price']))

          query = """
          UPDATE products
          SET stock = stock -%s
          WHERE id = %s
          """

          self.databasemanager.execute_query(query,(item['quantity'],item['product_id']))

       query = """
       DELETE FROM cart
       WHERE user_id = %s
       """

       self.databasemanager.execute_query(query,(self.user_id,))
       self.databasemanager.commit()
       return f"Order Placed Successfully! Total = ₹{total_amount}"
      except Exception as e:

       self.databasemanager.rollback()

       return f"Checkout Failed: {e}"