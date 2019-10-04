# flask-apis

###### Contains APIs for managing Clusters & Machines.

##### Python Interpreter used - python3.6

##### pypi requirements

* Flask==1.1.1

##### How to execute Project

`$ python3.6 runapp.py`

#### APIs

- Cluster Create API
  - URL - 127.0.0.1:8000/cluster/create
  - Method - POST
  - Content-Type - application/x-www-form-urlencoded
  - Form Data
    - cluster_name: str (example: cluster1)
    - cloud_region: str (example: Asia/Kolkata)


- Cluster Details API
  - URL - 127.0.0.1:8000/cluster/details
  - Method - POST/GET


- Cluster Details by Id API
  - URL - 127.0.0.1:8000/cluster/details/<cluster_id>
  - Method - POST/GET


- Machine Create API
  - URL - 127.0.0.1:8000/machine/create
  - Method - POST
  - Content-Type - application/x-www-form-urlencoded
  - Form Data
    - cluster_name: str (example: cluster1)
    - machine_name: str (example: machine1)
    - ip_address:   str (example: 127.0.0.1:7865)
    - instance_type: str (example: type1)


- Cluster Details API
  - URL - 127.0.0.1:8000/machine/details
  - Method - POST/GET


- Cluster Details by Id API
  - URL - 127.0.0.1:8000/machine/details/<machine_id>
  - Method - POST/GET
