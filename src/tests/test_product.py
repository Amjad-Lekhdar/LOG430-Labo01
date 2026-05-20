from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    product = Product(None, "Test Product", "Test Brand", 19.99)
    dao.insert(product)
    product_list = dao.select_all()
    assert len(product_list) >= 4

def test_product_update():
    product = Product(None, "Test Product", "Test Brand", 19.99)
    assigned_id = dao.insert(product)
    assert assigned_id is not None

def test_product_delete():
    product = Product(None, "Test Product", "Test Brand", 19.99)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)
    product_list = dao.select_all()
    assert len(product_list) >= 4