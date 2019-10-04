from flask import Flask
from flask import request

import json
from Components.Cluster import Cluster
from Components.Machine import Machine

app = Flask(__name__)
host = "127.0.0.1"
port = 8000


def json_response(data, status, is_error=False):
    if type(data) == dict:
        if is_error:
            data["success"] = False
        return app.response_class(
            response=json.dumps(data, sort_keys=True, indent=2),
            status=status,
            mimetype="application/json"
        )

    return data


def check_for_required_keys(data):
    if type(data) != dict:
        raise Exception("Invalid Data Received")
    for key, value in data.items():
        if value is None:
            raise KeyError(key)


@app.route('/cluster/create', methods=['POST'])
def cluster_create():
    try:

        data = dict()
        data['cluster_name'] = request.form.get("cluster_name")
        data['cloud_region'] = request.form.get("cloud_region")
        check_for_required_keys(data)

        cluster = Cluster()
        cluster.add_cluster(data)

        return json_response({"status": True}, 200)

    except KeyError as e:
        return json_response({"success": False, "error": 'one/more key missing from data. {} missing'.format(e)}, 500)

    except TypeError as e:
        return json_response({"success": False, "error": 'TypeError: '.format(e)}, 500)

    except Exception as e:
        return json_response({"success": False, "error": str(e)}, 500)


@app.route('/cluster/details', methods=['POST', 'GET'])
def cluster_details():
    try:
        cluster = Cluster()
        result = cluster.fetch_clusters()

        return json_response({"status": True, "data": result}, 200)

    except KeyError as e:
        return json_response({"success": False, "error": 'one/more key missing from data. {} missing'.format(e)}, 500)

    except TypeError as e:
        return json_response({"success": False, "error": 'TypeError: '.format(e)}, 500)

    except Exception as e:
        return json_response({"success": False, "error": str(e)}, 500)


@app.route('/cluster/details/<cluster_id>', methods=['POST', 'GET'])
def cluster_details_with_id(cluster_id):
    try:
        cluster = Cluster()
        result = cluster.fetch_clusters(id=cluster_id)

        return json_response({"status": True, "data": result}, 200)

    except KeyError as e:
        return json_response({"success": False, "error": 'one/more key missing from data. {} missing'.format(e)}, 500)

    except TypeError as e:
        return json_response({"success": False, "error": 'TypeError: '.format(e)}, 500)

    except Exception as e:
        return json_response({"success": False, "error": str(e)}, 500)


@app.route('/machine/create', methods=['POST'])
def machine_create():
    try:

        data = dict()
        data['machine_name'] = request.form.get("machine_name")
        data['ip_address'] = request.form.get("ip_address")
        data['instance_type'] = request.form.get("instance_type")
        data['cluster_name'] = request.form.get("cluster_name")

        check_for_required_keys(data)

        machine = Machine()
        machine.add_machine(data)

        return json_response({"status": True}, 200)

    except KeyError as e:
        return json_response({"success": False, "error": 'one/more key missing from data. {} missing'.format(e)}, 500)

    except TypeError as e:
        return json_response({"success": False, "error": 'TypeError: '.format(e)}, 500)

    except Exception as e:
        return json_response({"success": False, "error": str(e)}, 500)


@app.route('/machine/details', methods=['POST', 'GET'])
def machine_details():
    try:
        machine = Machine()
        result = machine.fetch_machines()

        return json_response({"status": True, "data": result}, 200)

    except KeyError as e:
        return json_response({"success": False, "error": 'one/more key missing from data. {} missing'.format(e)}, 500)

    except TypeError as e:
        return json_response({"success": False, "error": 'TypeError: '.format(e)}, 500)

    except Exception as e:
        return json_response({"success": False, "error": str(e)}, 500)


@app.route('/machine/details/<machine_id>', methods=['POST', 'GET'])
def machine_details_by_id(machine_id):
    try:
        machine = Machine()
        result = machine.fetch_machines(id=machine_id)

        return json_response({"status": True, "data": result}, 200)

    except KeyError as e:
        return json_response({"success": False, "error": 'one/more key missing from data. {} missing'.format(e)}, 500)

    except TypeError as e:
        return json_response({"success": False, "error": 'TypeError: '.format(e)}, 500)

    except Exception as e:
        return json_response({"success": False, "error": str(e)}, 500)


# Keep this at end of file only
if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
