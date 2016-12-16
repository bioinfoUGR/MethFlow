#!/usr/bin/env python3

import os, sys, yaml, dialog, PyZenity
from urllib.request import urlretrieve, urlopen

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
    os.chdir('/tmp')
    url = 'http://bioinfo2.ugr.es/MethFlow/assemblies/assemblies.txt'
    response = urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    text = text.strip().split('\n')
    if not settings.assemblies:
        assemblies = os.path.join(getattr(settings, 'shared'), 'assemblies')
        if not os.path.exists(assemblies):
            os.makedirs(assemblies)
        setattr(settings, 'assemblies', assemblies)
    msg = 'Please select assemblies to download. They will be downloaded into the assemblies folder.'
    select_title = "MethFlow Data Downloader"
    if os.environ['DISPLAY']:
        choices = []
        for line in text:
            choices.append(['http://bioinfo2.ugr.es/MethFlow/assemblies/' + line.strip() + '.tar.gz', line.strip()])
        tags = PyZenity.List(['Select', 'Assembly'], title = select_title, text = msg, boolstyle = 'checklist', data = choices)
        for value in choices:
            if value[1] in tags:
                print(value[0])  
    else:
        choices = []
        for line in text:
            choices.append(['http://bioinfo2.ugr.es/MethFlow/assemblies/' + line.strip() + '.tar.gz', line.strip(), False])
        choices[0][2] = True
        d = dialog.Dialog(autowidgetsize = True)
        d.set_background_title(select_title)
        code, tags = d.checklist(msg, choices = choices, ok_label = "SELECT", no_cancel = True, no_tags = True)
        if code == 'esc':
            code = logs.print_info('Leaving MethFlow Settings...', isdialog)
            os.system('clear')
            raise SystemExit
        else:
            for tag in tags:
                fname = tag.replace('http://bioinfo2.ugr.es/MethFlow/assemblies/', '')
                fname = os.path.join(settings.assemblies, fname)
                urlretrieve(tag, fname, reporthook)
                os.system('tar -xf {fname} && rm {fname}'.format(fname = fname))
            os.system('clear')
