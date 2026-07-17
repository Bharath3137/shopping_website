class ProductManager:

    def __init__(self, databasemanager):
        self.databasemanager = databasemanager

    def get_all_products(self):
        query = "SELECT * FROM products"
        return self.databasemanager.execute_query(query)

    def get_product(self, product_id):
        query = "SELECT * FROM products WHERE id=%s"
        products = self.databasemanager.execute_query(query,(product_id,))

        if products:
            return products[0]
        return None

    def is_valid_product(self, product_id):
        return self.get_product(product_id) is not None

    def search_product(self, name):
        query = "SELECT * FROM products WHERE name=%s"
        return self.databasemanager.execute_query(query,(name,))

    def add_product(self, name, price, stock, category):

        query = """
        INSERT INTO products(name, price, stock, category)
        VALUES(%s,%s,%s,%s)
        """

        self.databasemanager.execute_query(query,(name,price,stock,category))

        return "Product Added Successfully"

    def update_product(self, product_id, field, value):

        if not self.is_valid_product(product_id):
            return "Product Not Found"

        if isinstance(value, str):
            value = f"'{value}'"

        query = f"""
        UPDATE products
        SET {field}=%s
        WHERE id=%s
        """

        self.databasemanager.execute_query(query,(product_id,value))

        return "Product Updated Successfully"

    def delete_product(self, product_id):

        if not self.is_valid_product(product_id):
            return "Product Not Found"

        query = "DELETE FROM products WHERE id=%s"

        self.databasemanager.execute_query(query,(product_id,))

        return "Product Deleted Successfully"