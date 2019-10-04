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

    def fetch_by_name(self, cluster_name):
        db = SqlDB()
        db.create_connection()
        result = db.fetch_with_condition(table_name=self.db_table, condition={"cluster_name": cluster_name})

        if type(result) == str:
            raise Exception(result)

        db.close_connection()
        return result

    def delete(self):
        db = SqlDB()
        db.create_connection()
        result = db.delete(table_name=self.db_table, condition={"cluster_id": self.cluster_id})

        if type(result) == str:
            raise Exception(result)

        db.close_connection()
        return result


class MachineModel:
    machine_id = int
    machine_name = str
    ip_address = str
    instance_type = str
    cluster_id = int
    machine_status = str
    db_table = "machine_details"

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
        result = db.fetch_with_condition(table_name=self.db_table, condition={"machine_id": id})

        if type(result) == str:
            raise Exception(result)

        db.close_connection()
        return result

    def fetch_by_status(self, status):
        if status not in ["start", "stop", "reboot"]:
            raise Exception("Invalid Status Data")

        db = SqlDB()
        db.create_connection()
        result = db.fetch_with_condition(table_name=self.db_table, condition={"machine_status": status})

        if type(result) == str:
            raise Exception(result)

        db.close_connection()
        return result

    def delete(self):
        db = SqlDB()
        db.create_connection()
        result = db.delete(table_name=self.db_table, condition={"machine_id": self.machine_id})

        if type(result) == str:
            raise Exception(result)

        db.close_connection()
        return result


class TagModel:
    tag_id = int
    machine_id = int
    tag_name = str
    db_table = "tag_details"

    def insert(self):
        db = SqlDB()
        db.create_connection()
        result = db.insert_operation(table_name=self.db_table, value_data=[self.__dict__])

        if type(result) == str:
            raise Exception(result)

        db.close_connection()

    def fetch_all_tags(self):
        db = SqlDB()
        db.create_connection()
        result = db.fetch_unique(table_name=self.db_table, uniq=["tag_name"])

        if type(result) == str:
            raise Exception(result)

        db.close_connection()
        return result

    def fetch_by_tag_name(self, tag_name):

        db = SqlDB()
        db.create_connection()
        result = db.fetch_with_condition(table_name=self.db_table, condition={"tag_name": tag_name})

        if type(result) == str:
            raise Exception(result)

        db.close_connection()
        return result


