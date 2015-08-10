from XRootD import client
from XRootD import File as XFile
import xrootdfs
import fs.filelike

class XRootDFile(fs.filelike.FileLikeBase):

    def __init__(self, bufsize=1024*64):
        super(XRootDFile, self).__init__(bufsize)

    def seek(self, offset, whence=0):
        self._ifp = offset

    def read(self, size=0, offset=None, timeout=0, callback=None):
        if offset=None:
            offset=self._ifp
        return self._file.read(offset, size, timeout, callback)

    def tell():
        pass

    def truncate(size=None):
        pass

    def write(string):
        pass