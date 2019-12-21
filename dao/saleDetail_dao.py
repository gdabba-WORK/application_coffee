import inspect

from mysql.connector import Error

from dao.abs_dao import Dao

insert_sql = "Insert into sale_detail values(%s, %s, %s, %s, %s)"
update_sql = "UPDATE sale_detail SET salePrice=%s, addTax=%s, supplyPrice=%s, marginPrice=%s WHERE no=%s"
delete_sql = "DELETE FROM sale_detail WHERE no=%s"
select_sql = "SELECT no, salePrice, addTax, supplyPrice, marginPrice FROM sale_detail"
select_sql_where = select_sql + " WHERE no=%s"


class SaleDetailDao(Dao):
    def insert_item(self, no=None, salePrice=None, addTax=None, supplyPrice=None, marginPrice=None):
        print("\n______{}()______".format(inspect.stack()[0][3]))
        args = (no, salePrice, addTax, supplyPrice, marginPrice)
        try:
            super().do_query(query=insert_sql, kargs=args)
            return True
        except Error:
            return False

    def update_item(self, salePrice=None, addTax=None, supplyPrice=None, marginPrice=None, no=None):
        print("\n______{}()______".format(inspect.stack()[0][3]))
        args = (salePrice, addTax, supplyPrice, marginPrice, no)
        try:
            self.do_query(query=update_sql, kargs=args)
            return True
        except Error:
            return False

    def delete_item(self, no=None):
        print("\n______{}()______".format(inspect.stack()[0][3]))
        args = (no,)
        try:
            self.do_query(query=delete_sql, kargs=args)
            return True
        except Error:
            return False

    def select_item(self, no=None):
        print("\n______{}()______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(select_sql) if no is None else cursor.execute(select_sql_where, (no,))
            res = []
            [res.append(row) for row in self.iter_row(cursor, 5)]
            return res
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
