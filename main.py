from dao.product_dao import ProductDao
from db_connection.connection_pool_ import ConnectionPool

if __name__ == "__main__":
    pool = ConnectionPool.get_instance()
    connection = pool.get_connection()

    print(pool, connection)

    pdt = ProductDao()
    # pdt.insert_product()
    pdt.delete_product()
    pdt.select()
    pdt.update_product()