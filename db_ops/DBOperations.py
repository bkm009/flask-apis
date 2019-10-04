import sqlite3
import os


# Accessing Result in Dict Format
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class SqlDB:

    def __init__(self):
        conn = None

    def turn_on_foreign_key(self):
        self.conn.execute("PRAGMA foreign_keys=ON ;")
        self.conn.commit()

    def create_connection(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        self.conn = sqlite3.connect(database='{}/sqlite_db'.format(dir), timeout=60)
        self.turn_on_foreign_key()
        return True

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
        return True

    def insert_operation(self, table_name=None, value_data=[]):

        try:
            if len(value_data) == 0:
                raise Exception("No data to Insert")

            columns = tuple([x for x in value_data[0].keys()])
            query = "INSERT INTO `{}` {} VALUES ".format(table_name, columns)
            for x in value_data:
                query += "("
                for y in columns:
                    query += "'{}',".format(x[y])
                query = query[:-1] + "),"

            query = query[:-1]
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()

            return True

        except sqlite3.OperationalError as e:
            return "{}".format(e)

        except Exception as e:
            return "{}".format(e)

    def fetch_all(self, table_name=None):

        try:
            self.conn.row_factory = dict_factory
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM `{}` ;".format(table_name))
            result = cursor.fetchall()
            return result

        except sqlite3.OperationalError as e:
            return "{}".format(e)

        except Exception as e:
            return "{}".format(e)

    def fetch_with_condition(self, table_name=None, condition={}):

        try:

            query = "SELECT * FROM `{}` ".format(table_name)
            if len(condition.keys()) > 0:
                query += "WHERE "
                temp = []
                for key in condition.keys():
                    if type(condition[key]) != tuple:
                        temp.append("{}=:{}".format(key, key))
                    else:
                        temp.append("{} IN {}".format(key, condition[key]))

                query += " AND ".join(temp)

            self.conn.row_factory = dict_factory
            cursor = self.conn.cursor()
            cursor.execute(query, condition)
            result = cursor.fetchall()
            return result

        except sqlite3.OperationalError as e:
            return "{}".format(e)

        except Exception as e:
            return "{}".format(e)

    def fetch_unique(self, table_name=None, uniq=[]):
        try:

            if len(uniq) == 0:
                raise Exception("No Column Given")

            query = "SELECT DISTINCT {} FROM `{}` ".format(",".join(uniq), table_name)
            self.conn.row_factory = dict_factory
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result

        except sqlite3.OperationalError as e:
            return "{}".format(e)

        except Exception as e:
            return "{}".format(e)

    def delete(self, table_name=None, condition={}):
        try:

            query = "DELETE FROM `{}` ".format(table_name)
            if len(condition.keys()) > 0:
                query += "WHERE "
                temp = []
                for key in condition.keys():
                    temp.append("{}=:{}".format(key, key))

                query += " AND ".join(temp)

            self.conn.row_factory = dict_factory
            cursor = self.conn.cursor()
            cursor.execute(query, condition)
            self.conn.commit()
            return True

        except sqlite3.OperationalError as e:
            return "{}".format(e)

        except Exception as e:
            return "{}".format(e)

    def update_data(self, table_name=None, data_to_update={}, condition={}):

        try:
            query = "UPDATE `{}` ".format(table_name)
            if len(data_to_update.keys()) > 0:
                query += "SET "
                temp = []
                for key in data_to_update.keys():
                    temp.append("{}=:{}".format(key, key))

                query += " , ".join(temp)

            if len(condition.keys()) > 0:
                query += " WHERE "
                temp = []
                for key in condition.keys():
                    if type(condition[key]) != tuple:
                        temp.append("{}=:{}".format(key, key))
                    else:
                        temp.append("{} IN {}".format(key, condition[key]))

                query += " AND ".join(temp)

            for key, value in data_to_update.items():
                condition[key] = value

            self.conn.row_factory = dict_factory
            cursor = self.conn.cursor()
            cursor.execute(query, condition)
            self.conn.commit()
            return True

        except sqlite3.OperationalError as e:
            return "{}".format(e)

        except Exception as e:
            return "{}".format(e)