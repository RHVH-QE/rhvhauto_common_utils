import uuid

import pytest


@pytest.fixture(scope="module")
def api(rhvurl):
    from rhvhauto_common_utils.rhv.base import BaseRhvAPI
    return BaseRhvAPI(rhvurl)


def test_version():
    from rhvhauto_common_utils import __version__
    assert __version__ == '0.1.2'


# =========================================================
# ================ Test Cases =============================
# =========================================================
class TestDataCenter:
    """data center tests"""
    DC_NAME = f"atv_dc_test_{uuid.uuid4().hex[:8]}"

    def test_add_data_center(self, api):
        dc_id = api.add_data_center(self.DC_NAME, local=False)
        assert "-" in dc_id
        assert len(dc_id.split("-")) == 5

    def test_find_data_center(self, api):
        dc_id = api.find_data_center(self.DC_NAME)
        assert "-" in dc_id
        assert len(dc_id.split("-")) == 5

    def test_del_data_center(self, api):
        ret = api.del_data_center(self.DC_NAME)
        assert ret is None


class TestCluster:
    """cluster related tests"""

    def test_cluster_supported_cpu_types(self, api):
        ret = api.cluster_supported_cpu_types(level="4.4")
        assert type(ret) is list
        assert len(ret) > 0


class TestStorage:
    """"""


class TestVM:
    """"""
    VM_NAME = "atv_vm_02"
    CLUSTER_NAME = "atv_cl_02"
    TPL_NAME = "Blank"

    def test_add_vm(self, api):
        vm = api.add_vm(self.VM_NAME, cluster_name=self.CLUSTER_NAME, template_name=self.TPL_NAME)
        assert vm.name == self.VM_NAME
