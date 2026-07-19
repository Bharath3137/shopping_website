class DashboardManager:

    def __init__(self, databasemanager):
        self.databasemanager = databasemanager

    def get_dashboard(self):

        dashboard = {}

        query = """
        SELECT COUNT(*) AS total_users
        FROM users
        """
        result = self.databasemanager.execute_query(query)
        dashboard["total_users"] = result[0]["total_users"]

        query = """
        SELECT COUNT(*) AS total_products
        FROM products
        """
        result = self.databasemanager.execute_query(query)
        dashboard["total_products"] = result[0]["total_products"]

        query = """
        SELECT COUNT(*) AS total_orders
        FROM orders
        """
        result = self.databasemanager.execute_query(query)
        dashboard["total_orders"] = result[0]["total_orders"]

        query = """
        SELECT SUM(total_amount) AS total_revenue
        FROM orders
        """
        result = self.databasemanager.execute_query(query)

        dashboard["total_revenue"] = (
            result[0]["total_revenue"] if result[0]["total_revenue"] is not None else 0
        )

        query = """
        SELECT products.name,SUM(order_items.quantity) AS sold FROM order_items
        JOIN products
        ON order_items.product_id = products.id
        GROUP BY products.id, products.name
        ORDER BY sold DESC
        LIMIT 5
        """

        dashboard["top_products"] = self.databasemanager.execute_query(query)

        return dashboard
