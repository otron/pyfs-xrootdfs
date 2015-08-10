import pytest
from XRootD import client
from XRootD.client.flags import OpenFlags

from configobj import ConfigObj
cfg = ConfigObj('test/conf.cfg')['xrootd']

@pytest.fixture
def xrootd_client():
    return client.FileSystem(cfg['address'])

@pytest.fixture
def base_path():
    return cfg['home_dir'] + 'test/'

@pytest.fixture
def address():
    return cfg['address']

@pytest.fixture
def get_dirlist(client, path):
    return client.dirlist(path)[1]

class Test_Dirlist():

    def test_dirlist(self, xrootd_client, base_path):
        # get the dirlisting via pyxrootd
        xdc = xrootd_client
        status, listing = xdc.dirlist(base_path)

        # this directory is initially empty
        assert len(listing.dirlist) == 1
        #for e in listing:
            #print "{0} {1:>10} {2}".format(e.statinfo.modtimestr, entry.statinfo.size, entry.name)
        assert 2 == 2

class Test_Stuff():

    def test_filecreation(self, xrootd_client, base_path):
        # get dirlist, save value
        xdc = xrootd_client
        listing = get_dirlist(xdc, base_path)
        print listing
        val_before = len(listing.dirlist)

        # create file
        fname = 'what'
        fpath = address()+'/'+base_path+fname
        with client.File() as f:
            # Cleanup not needed: DELETE flag replaces existing file, if any.
            print f.open(fpath, OpenFlags.DELETE)
            f.write('youse\ncannot\nbe\nfor\nreals,\nhuh?')
            f.close()

        listing = get_dirlist(xdc, base_path)
        assert len(listing.dirlist) == val_before+1
