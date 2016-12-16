#!/usr/bin/env python3

import os, yaml, dialog, PyZenity

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

def turn_off():
    os.system('cp /home/methflow/.bashrc /home/methflow/.bashrc_backup')
    with open('/home/methflow/.bashrc_backup','rt') as i:
        with open('/home/methflow/.bashrc','wt') as o:
            for line in i:
                if line.startswith('first_login'):
                    line = '#' + line
                o.write(line)

if __name__ == '__main__':
    settings = yaml.load(open('/home/methflow/.methflowrc', 'rt').read())
    msg = "Please configure your keyboard layout and select a shared folder.\nMethFlow will use this folder as the working directory."
    select_title = "Select a shared folder"
    if os.environ['DISPLAY']:
        msg = "<b>Welcome to MethFlowVM!</b>\n\n" + msg
        code = PyZenity.InfoMessage(msg)
        os.popen('xfce4-keyboard-settings').read()
        dpath = PyZenity.GetDirectory(title = select_title, selected = '/media/')
        dpath = dpath[0]
        if os.path.isdir(dpath):
            setattr(settings, 'shared', dpath)
        with open('/home/methflow/.methflowrc', 'wt') as handle:
            handle.write(yaml.dump(settings, default_flow_style = False))
        turn_off()
    else:
        msg = "\ZbWelcome to MethFlowVM!\ZB \n\n" + msg
        d = dialog.Dialog(autowidgetsize = True)
        d.set_background_title("MethFlow Settings")
        d.msgbox(msg, colors=True)
        os.system('sudo dpkg-reconfigure keyboard-configuration')
        code, dpath = d.dselect('/media/', title = select_title, ok_label = "SELECT", no_cancel = True)
        if code == 'esc':
            os.system('clear')
            raise SystemExit
        else:
            os.system('clear')
            if os.path.isdir(dpath):
                setattr(settings, 'shared', dpath)
            with open('/home/methflow/.methflowrc', 'wt') as handle:
                handle.write(yaml.dump(settings, default_flow_style = False))
            turn_off()

