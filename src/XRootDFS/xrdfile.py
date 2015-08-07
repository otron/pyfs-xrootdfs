from XRootD import client
import xrootdfs
import fs.filelike

class XRootDFile(fs.filelike.FileLikeBase):

    def __init__(self, bufsize=1024*64):
        super(XRootDFile, self).__init__(bufsize)
