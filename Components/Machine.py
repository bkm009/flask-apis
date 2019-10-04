from db_ops.ModelLayer import MachineModel
from db_ops.ModelLayer import ClusterModel
from db_ops.ModelLayer import TagModel


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

        return {"success": True, "message": "Machine Added Successfully"}

    def fetch_machines(self, id=None, status=None):
        machine = MachineModel()
        if id is not None:
            result = machine.fetch_by_id(id=id)
            return result
        elif status is not None:
            result = machine.fetch_by_status(status=status)
            return result
        else:
            result = machine.fetch_all()
            return result

    def fetch_machine_with_tag(self, tag_name=None):
        if tag_name is None:
            raise Exception("No Tag Given")

        tag = TagModel()
        result = tag.fetch_by_tag_name(tag_name=tag_name)

        if len(result) == 0:
            raise Exception("No Entry with given Tag Name")

        machine_ids = tuple([x.get("machine_id") for x in result])
        if len(result) == 1:
            machine_ids = (result[0]["machine_id"])

        machine = MachineModel()
        result = machine.fetch_by_id(id=machine_ids)
        return result

    def delete_machine(self, data):
        machine = MachineModel()
        for key, value in data.items():
            machine.__setattr__(key, value)

        machine.delete()

        return {"success": True, "message": "Machine Deleted Successfully"}

    def operate(self, data):
        result = self.fetch_machine_with_tag(tag_name=data['tag_name'])

        if len(result) == 0:
            raise Exception("No Entry with given Tag Name")

        machine_ids = tuple([x.get("machine_id") for x in result])
        if len(result) == 1:
            machine_ids = (result[0]["machine_id"])

        machine = MachineModel()
        machine.set_operation(id=machine_ids, operation=data["operation"])

        return {"success": True, "message": "Status Updated Successfully"}
