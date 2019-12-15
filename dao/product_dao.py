from dml.connection_pool import ConnectionPool
from mysql.connector import Error


class ProductDao():
    def __init__(self):
        pass

    # __do_query()
    def __do_query(self, query=None, arg=None):
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute(query, arg)
            conn.commit()
        except Error as error:
            print(error)
            raise error
        finally:
            cursor.close()
            conn.close()

    # insert
    def insert_product(self, code, name):
        insert_sql = "Insert into product values(%s, %s)"
        args = (code, name)
        self.__do_query(query=sql, arg=args)

    # select
    def __iter_row(cursor, size=5):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    # python_mysql_study 프로젝트-dml패키지-Fetch_Query파일의 query_with_fetchmany()와 같다
    def select_product(sql):
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)

            # 아래 2줄 추가됨
            data = []
            [data.append(row) for row in self.__iter_row(cursor, 5)]
            # for row in __iter_row(cursor, 5):
                # print(type(row), " ", row)
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    # update
    def update_product(self, sql, name, code):
        args = (name, code)
        try:
            self.__do_query(query=sql, arg=args)
            return True
        except Error as e:
            return False

    # delete
    def delete_product(self, sql, code):
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (code,))
            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()