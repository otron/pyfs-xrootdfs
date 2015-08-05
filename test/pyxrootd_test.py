import pytest
from XRootD import client

from configobj import ConfigObj
cfg = ConfigObj('test/conf.cfg')['system']

@pytest.fixture
def xrootd_client():
    return client.FileSystem(cfg['address'])

class Test_Dirlist():

    def test_what(self, xrootd_client):
        pass
