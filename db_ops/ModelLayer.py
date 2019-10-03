from .DBOperations import SqlDB


class ClusterModel:
    cluster_id = int
    cluster_name = str
    cloud_region = str
    db_table = "cluster_details"

    def insert(self):
        db = SqlDB()
        db.create_connection()
        result = db.insert_operation(table_name=self.db_table, value_data=[self.__dict__])

        if type(result) == str:
            raise Exception(result)

        db.close_connection()

    def fetch_all(self):
        db = SqlDB()
        db.create_connection()
        result = db.fetch_all(table_name=self.db_table)

        if type(result) == str:
            raise Exception(result)

        db.close_connection()
        return result

    def fetch_by_id(self, id):
        db = SqlDB()
        db.create_connection()
        result = db.fetch_with_condition(table_name=self.db_table, condition={"cluster_id": id})

        if type(result) == str:
            raise Exception(result)

        db.close_connection()
        return result
