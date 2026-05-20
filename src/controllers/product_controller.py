from daos.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self.dao = ProductDAO()

    def list_products(self):
        """ List all products """
        return self.dao.select_all()
        
    def create_product(self, product):
        """ Create a new product based on user inputs """
        self.dao.insert(product)

    def shutdown(self):
        """ Close database connection """
        self.dao.close()