import pytest
from XRootD import client
from XRootD.client.flags import OpenFlags

import uuid

### Fixtures
@pytest.fixture
def xrootd_client(cfg):
    return client.FileSystem(cfg['xrootd']['address'])

@pytest.fixture
def test_dir(cfg):
    return cfg['xrootd']['home_dir'] + 'test/'

@pytest.fixture
def address(cfg):
    return cfg['xrootd']['address']

@pytest.fixture
def full_path(cfg):
    return address(cfg) + '/' + test_dir(cfg)

def get_dirlist(client, path):
    return client.dirlist(path)[1]


### Tests
class Test_Dirlist():

    def test_dirlist(self, xrootd_client, test_dir):
        # get the dirlisting via pyxrootd
        xdc = xrootd_client
        status, listing = xdc.dirlist(test_dir)

        # this directory is initially empty
        #assert len(listing.dirlist) == 
        #for e in listing:
            #print "{0} {1:>10} {2}".format(e.statinfo.modtimestr, entry.statinfo.size, entry.name)
        assert 2 == 2

class Test_Stuff():

    def test_filecreation(self, xrootd_client, test_dir, address):
        # get dirlist, save value
        xdc = xrootd_client
        listing = get_dirlist(xdc, test_dir)
        val_before = len(listing.dirlist)

        # create file using NEW flag
        # requires that the file doesn't already exist
        fname = str(uuid.uuid4())
        fpath = address+'/'+test_dir+fname
        with client.File() as f:
            f.open(fpath, OpenFlags.NEW)
            f.write('youse\ncannot\nbe\nfor\nreals,\nhuh?')
            f.close()

        listing = get_dirlist(xdc, test_dir)
        assert len(listing.dirlist) == val_before+1

        # cleanup
        xdc.rm(test_dir+fname)
        assert len(get_dirlist(xdc, test_dir).dirlist) == val_before

    def test_opening(self, full_path, rnd_fname):
        fname = rnd_fname
        status, f = client.File().open(full_path+fname, OpenFlags.READ)
        assert status.ok == False
        assert status.error == True
