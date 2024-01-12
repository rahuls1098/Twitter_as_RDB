import mysql.connector as connector

# Instantiate a connection to the database
class DBConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cur = None

    def get_connection(self):
        """
        :return: Get connection to database
        """
        if self.conn is None:
            try:
                self.conn = connector.connect(host=self.host, user=self.user, passwd=self.password, database=self.database)
                return self.conn
            except Exception as e:
                print(e)
        return self.conn

    def get_cursor(self):
        """
        :return: Get cursor object
        """
        try:
            self.cur = self.conn.cursor(buffered=True)
            return self.cur
        except Exception as e:
            print(e)

    def execute_query(self, query):
        """
        :param query: Query to be executed
        :return: result of executed query
        """
        try:
            self.cur.execute(query)
            return self.cur
        except Exception as e:
            print(e)

    def commit(self):
        """
        :return: Perform commit to database
        """
        try:
            self.conn.commit()
        except Exception as e:
            print(e)

    def close_connection(self):
        """
        :return: Closed connection
        """
        if self.conn is not None:
            try:
                self.conn = connector.close()
                return self.conn
            except Exception as e:
                print(e)




