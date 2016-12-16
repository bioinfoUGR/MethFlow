#!/usr/bin/env python3

import os, sys, yaml
from urllib.request import urlretrieve

class Settings_obj(yaml.YAMLObject):
    
    yaml_tag = u'!MethFlow_Settings'
    
    def __init__(self, **kwargs):
        variables = ['shared', 'assemblies', 'adapters', 'output']
        for var in variables:
            if var in kwargs:
                setattr(self, var, kwargs[var])
            else:
                if var == 'shared':
                    setattr(self, var, '/home/methflow')
                else:
                    setattr(self, var, None)

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))

if __name__ == '__main__':
    settings = yaml.load(open('/home/methflow/.methflowrc', 'rt').read())
    url = 'http://bioinfo2.ugr.es/MethFlow/test_datasets.tar.gz'
    fname = os.path.join(settings.shared, 'test_datasets.tar.gz')
    urlretrieve(url, fname, reporthook)
    os.system('tar -xf {fname} && rm {fname}'.format(fname = fname))

