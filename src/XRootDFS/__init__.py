# I guess this is how python projects work?

import fs.base
from XRootD import client

class XRootDFS(fs.base.FS):
    def __init__(self, addr, path='/'):
        self.fs = client.FileSystem(addr)
        self.path = path
