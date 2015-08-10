import pytest
from XRootD import client

from configobj import ConfigObj
cfg = ConfigObj('test/conf.cfg')['system']

@pytest.fixture
def xrootd_client():
    return client.FileSystem(cfg['address'])

@pytest.fixture
def base_path():
    return cfg['home_dir'] + 'test/'

class Test_Dirlist():

    def test_dirlist(self, xrootd_client, base_path):
        # get the dirlisting via pyxrootd
        xdc = xrootd_client
        status, listing = xdc.dirlist(base_path)

        # this directory is initially empty
        assert len(listing.dirlist) == 0
        #for e in listing:
            #print "{0} {1:>10} {2}".format(e.statinfo.modtimestr, entry.statinfo.size, entry.name)
        assert 2 == 2
