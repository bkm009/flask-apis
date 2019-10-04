from db_ops.ModelLayer import MachineModel
from db_ops.ModelLayer import ClusterModel


class Machine:

    def add_machine(self, data):

        cluster = ClusterModel()
        if "cluster_name" not in data:
            raise KeyError("cluster_name")

        result = cluster.fetch_by_name(cluster_name=data.get("cluster_name"))

        if len(result) != 1:
            raise Exception("Invalid Cluster Name")

        del data["cluster_name"]
        data["cluster_id"] = result[0]["cluster_id"]

        machine = MachineModel()
        for key, value in data.items():
            machine.__setattr__(key, value)

        machine.insert()

        return {"success": True, "message": "Cluster Added Successfully"}

    def fetch_machines(self, id=None):
        machine = MachineModel()
        if id is None:
            result = machine.fetch_all()
            return result
        else:
            result = machine.fetch_by_id(id=id)
            return result
