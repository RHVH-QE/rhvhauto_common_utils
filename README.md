# Common utils for RHVH automation project

## Prerequisite

- Python == "^3.7"

use `poetry` for dependency management and packaging

### For dev

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