# Common utils for RHVH automation project

## Prerequisite

- Python == "^3.7"

use `poetry` for dependency management and packaging

### For dev

- install dependencies

```
dnf install -y python3-devel libcurl-devel libxml-devel libxslt-devel
```

- install poetry

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

- then follow the [Document](https://python-poetry.org/docs/) for next setup

- cd to $PROJECT root

```
$> poetry install && poetry shell
```

for detail usage, please see [Document](https://python-poetry.org/docs/)

### use this package for other project

```
$> poetry add rhvhauto-common-utils
```

or

```
$> pip install rhvhauto-common-utils
```

## common_utils/rhv

a simple ovirt-sdk4 wrapper

<details>
<summary>HE Dashboard</summary>

- [x] add host
- [x] migrate vm

</details>

<details>
<summary>Upgrade</summary>

- [x] add data-center
- [x] remove data-center
- [x] add cluster
- [x] remove cluster
- [x] add host
- [x] list host
- [x] deactivate host
- [x] remove host
- [x] check_update_available
- [x] upgrade_host
- [x] update_network
- [ ] add_plain_storage_domain
- [ ] remove_storage_domain
- [x] create_vm_from_tpl
- [x] list_vm(self, vm_name)
- [x] start_vm(self, vm_name)
- [ ] operate_vm(self, vm_name, operation)
- [x] remove_vm(self, vm_name)
- [ ] create_vm_image_disk(self, vm_name, sd_name, disk_name, disk_size
- [ ] attach_disk_to_vm(self, disk_name, vm_name, bootable=False)
- [x] migrate_vm(self, vm_name)

</details>

## Examples

<details>
<summary>Basic Usage</summary>

```python
from rhvhauto_common_utils.rhv.base import BaseRhvAPI

if __name__ == '__main__':
    url = "https://FQDN/ovirt-engine/api"
    api = BaseRhvAPI(url)

    ret = api.add_data_center("atv_dc_01", local=False, wait=True)
    print(ret)

    ret = api.del_data_center("atv_dc_01")
    print(ret)

    ret = api.add_cluster(
        "atv_cl_01",
        data_center_name="atv_dc_01",
        cpu_type="Intel Skylake Server Family"
    )
    print(ret)

    ret = api.del_cluster("atv_cl_03")
    print(ret)

    ret = api.add_host(
        "atv_host_01",
        address="10.73.73.69",
        root_password="redhat",
        cluster_name="atv_cl_01",
        deploy_hosted_engine=False
    )
    print(ret)

    ret = api.deactivate_host("atv_host_01")
    print(ret)

    ret = api.activate_host('atv_host_01')
    print(ret)
    
    ret = api.add_iscsi_storage("name",
                                data_center_name="dc_name",
                                host_name="host_name",
                                lun_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                                address="0.0.0.0",
                                target="iqn.xxxxxxx:xxxx.xxxxxx.xxxxx",
                                port=3260)
    print(ret)
    
```

</details>
