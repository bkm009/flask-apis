from db_ops.ModelLayer import ClusterModel


class Cluster:

    def add_cluster(self, data):
        cluster = ClusterModel()
        for key, value in data.items():
            cluster.__setattr__(key, value)

        cluster.insert()

        return {"success": True, "message": "Cluster Added Successfully"}

    def fetch_clusters(self, id=None):
        cluster = ClusterModel()
        if id is None:
            result = cluster.fetch_all()
            return result
        else:
            result = cluster.fetch_by_id(id=id)
            return result
