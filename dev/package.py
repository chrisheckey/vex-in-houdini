name = 'vex_in_houdini'
version = '0.1.0'
description = 'https://classroom.cgmasteracademy.com/lecture/253824'
authors = [
    'chrisheckey@gmail.com'
]

requires = [
    'houdini-17',
    'subl',
    'vray_houdini',
    'dwfx_dev'
]

build_command = 'echo DEV PACKAGE INSTALLED: %REZ_BUILD_INSTALL_PATH%'


def post_commands():
    if defined('HOUDINI_VEX_PATH') and '&' not in getenv('HOUDINI_VEX_PATH'):
        env.HOUDINI_VEX_PATH.append('&')

    env.JOB = '{this.dev}/week1/hip'


def commands():
    env.HOUDINI_VEX_PATH.append('{this.dev}/week1/src/vex')


@early()
def dev():
    import os
    import inspect
    return os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe()))).replace('\\', '/')
