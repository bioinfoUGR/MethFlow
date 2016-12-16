#!/usr/bin/env python3

import os, yaml, dialog, argparse

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MethFlow Settings')
    parser.add_argument('shared_folder', help='Path of the shared folder', action='store', type=str)
    args = vars(parser.parse_args())
    settings = yaml.load(open('/home/methflow/.methflowrc', 'rt').read())
    if os.path.isdir(args['shared_folder']):
        setattr(settings, 'shared', os.path.abspath(args['shared_folder']))
    with open('/home/methflow/.methflowrc', 'wt') as handle:
        handle.write(yaml.dump(settings, default_flow_style = False))
