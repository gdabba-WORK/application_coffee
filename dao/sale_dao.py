import inspect

from mysql.connector import Error

from dao.abs_dao import Dao

insert_sql = "Insert into sale values(%s, %s, %s, %s, %s)"
update_sql = "UPDATE sale SET code=%s, price=%s, saleCnt=%s, marginRate=%s WHERE no=%s"
delete_sql = "DELETE FROM sale WHERE no=%s"
select_sql = "SELECT no, code, price, saleCnt, marginRate FROM sale"
select_sql_where = select_sql + " WHERE no=%s"


class SaleDao(Dao):
    def insert_item(self, no=None, code=None, price=None, saleCnt=None, marginRate=None):
        print("\n______{}()______".format(inspect.stack()[0][3]))
        args = (no, code, price, saleCnt, marginRate)
        try:
            super().do_query(query=insert_sql, kargs=args)
            return True,
        except Error as e:
            return False, e.msg

    def update_item(self, code=None, price=None, saleCnt=None, marginRate=None, no=None):
        print("\n______{}()______".format(inspect.stack()[0][3]))
        args = (code, price, saleCnt, marginRate, no)
        try:
            self.do_query(query=update_sql, kargs=args)
            return True,
        except Error as e:
            return False, e.msg

    def delete_item(self, no=None):
        print("\n______{}()______".format(inspect.stack()[0][3]))
        args = (no,)
        try:
            self.do_query(query=delete_sql, kargs=args)
            return True,
        except Error as e:
            return False, e.msg

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
            raise e
        finally:
            cursor.close()
            conn.close()