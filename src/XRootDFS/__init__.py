# I guess this is how python projects work?

import fs.base
from XRootD import client as xclient

class XRootDFS(fs.base.FS):
    def __init__(self, addr, path='/'):
        self.fs = xclient.FileSystem(addr)
        self.base_path = path

    def listdir(self, path='./'):
        status, res = self.fs.dirlist(self.base_path + path)
        return [unicode(e.name) for e in res]
