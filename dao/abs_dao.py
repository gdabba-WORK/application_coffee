import inspect
from abc import ABCMeta, abstractmethod

from mysql.connector import Error

from db_connection.connection_pool import ConnectionPool


class Dao(metaclass=ABCMeta):
    def __init__(self):
        self.connection_pool = ConnectionPool.get_instance()

    def iter_row(self, cursor, size=5):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def do_query(self, **kwargs):
        print("\n______ {}()______".format(inspect.stack()[0][3]))
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            cursor.execute(kwargs['query'], kwargs['kargs'])
            conn.commit()
        except Error as e:
            print(e)
            raise e
        finally:
            cursor.close()
            conn.close()

    @abstractmethod
    def insert_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def update_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def delete_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")
    @abstractmethod
    def select_item(self, **kwargs):
        raise NotImplementedError("Subclass must implement abstract method")


    # # __do_query()
    # def __do_query(self, query=None, arg=None):
    #     try:
    #         conn = ConnectionPool.get_instance().get_connection()
    #         cursor = conn.cursor()
    #         cursor.execute(query, arg)
    #         conn.commit()
    #     except Error as error:
    #         print(error)
    #         raise error
    #     finally:
    #         cursor.close()
    #         conn.close()
    #
    # # insert
    # def insert_product(self, code, name):
    #     insert_sql = "Insert into product values(%s, %s)"
    #     args = (code, name)
    #     self.__do_query(query=sql, arg=args)
    #
    # # select
    #

    #
    # # update
    # def update_product(self, sql, name, code):
    #     args = (name, code)
    #     try:
    #         self.__do_query(query=sql, arg=args)
    #         return True
    #     except Error as e:
    #         return False
    #
    # # delete
    # def delete_product(self, sql, code):
    #     try:
    #         conn = ConnectionPool.get_instance().get_connection()
    #         cursor = conn.cursor()
    #         cursor.execute(sql, (code,))
    #         conn.commit()
    #     except Error as error:
    #         print(error)
    #     finally:
    #         cursor.close()
    #         conn.close()
    #
    # # python_mysql_study 프로젝트-dml패키지-Fetch_Query파일의 query_with_fetchmany()와 같다
    # def select_product(sql):
    #     try:
    #         conn = ConnectionPool.get_instance().get_connection()
    #         cursor = conn.cursor()
    #         cursor.execute(sql)
    #
    #         # 아래 2줄 추가됨
    #         data = []
    #         [data.append(row) for row in self.__iter_row(cursor, 5)]
    #         # for row in __iter_row(cursor, 5):
    #             # print(type(row), " ", row)
    #     except Error as e:
    #         print(e)
    #     finally:
    #         cursor.close()
    #         conn.close()
